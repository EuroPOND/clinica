#!/usr/bin/python

def diffusion_preprocessing_SyN_based(in_dwi, in_T1, in_bvals, in_bvecs, working_directory, datasink_directory):
    """
    Create and run a high level pipeline to preprocess the DWI Images :
        - Preparation of the dataset
        - Correction for Head Motion 
        - Correction for Eddy Currents 
        - Correction for EPI susceptibility induced distortions using the SyN algorithm (SyB)
        - Bias field correction
    The outputs presented are tipically outputs necessary for further tractography.
    
    Inputs
    ---------
    in_dwi : STRING
      Path to the DWI image.
    in_T1: STRING
      Path to the T1 image.
    in_bvals: STRING
      Path to the b-vals text file.
    in_bvecs: STRING
      Path to the b-vecs text file.
    working_directory : STRING
      Directory to use as tmp for all the temporary files generated by the workflow.
    datasink_directory : STRING
      Base directory of the datasink.
    
    Outputs
    ----------
        DWI_hmc_ecc_sdc_bias_corrected - DWI corrected for Head motion, Eddy currents, EPI susceptibility induced distortions (syb) and bias field
        out_bvecs - updated and corrected gradient vectors table
        out_bvals - updated gradient values table
        mask_b0 - Binary mask obtained from the average of the B0 images    
    
    """
    
    import nipype.interfaces.io as nio
    import nipype.interfaces.utility as niu
    import nipype.pipeline.engine as pe
    import os.path as op
    import clinica.pipeline.preprocessing.dwi_corrections as predifcorrect

# Inputs existence checking

    inputs=[in_dwi, in_T1, in_bvals, in_bvecs, working_directory, datasink_directory]     
        
    for input_file in inputs:
        if not op.exists(input_file):
            raise IOError('file {} does not exist'.format(input_file))
    
    datasource = pe.Node(interface=nio.DataGrabber(infields=[], outfields=['dwi_image','bvectors_directions','bvalues','T1_image']), name='datasource')
    datasource.inputs.template = '*'
    datasource.inputs.field_template = dict(dwi_image= in_dwi,
                                            bvalues=in_bvals,
                                            bvectors_directions= in_bvecs,
                                            T1_image= in_T1)
    datasource.inputs.template_args = dict(dwi_image=[[]],
                                           bvalues=[[]],
                                           bvectors_directions=[[]],
                                           T1_image=[[]])
    datasource.inputs.sort_filelist = True
    
    inputnode = pe.Node(interface=niu.IdentityInterface(fields=["dwi_image", "bvectors_directions", "bvalues", 'T1_image']), name="inputnode")
    
    pre = predifcorrect.prepare_data(datasink_directory)
    
    hmc = predifcorrect.hmc_pipeline(datasink_directory)
    
    ecc = predifcorrect.ecc_pipeline(datasink_directory)

    sdc = predifcorrect.sdc_syb_pipeline(datasink_directory)

    bias = predifcorrect.remove_bias(datasink_directory)
    
    aac = predifcorrect.apply_all_corrections_syb(datasink_directory)
    
    datasink = pe.Node(nio.DataSink(), name='datasink_tracto')
    datasink.inputs.base_directory = op.join(datasink_directory, 'Outputs_for_Tractography/')
    
    wf = pe.Workflow(name='preprocess')
    wf.base_dir = working_directory
    
    wf.connect([(datasource, inputnode, [('dwi_image','dwi_image'), ('bvalues','bvalues'), ('bvectors_directions','bvectors_directions'), ('T1_image','T1_image')])])
    wf.connect([(inputnode, pre, [('dwi_image', 'inputnode.dwi_image'),
                                  ('bvalues', 'inputnode.bvalues'),
                                  ('bvectors_directions', 'inputnode.bvectors_directions')])])
    wf.connect([(pre, hmc,[('outputnode.dwi_b0_merge','inputnode.in_file'), ('outputnode.out_bvals','inputnode.in_bval'), ('outputnode.out_bvecs','inputnode.in_bvec')])])
    wf.connect([(pre, hmc, [('outputnode.mask_b0','inputnode.in_mask')])])
    wf.connect([(hmc, ecc, [('outputnode.out_xfms','inputnode.in_xfms'),('outputnode.out_file','inputnode.in_file')])])
    wf.connect([(pre, ecc, [('outputnode.out_bvals','inputnode.in_bval')])])
    wf.connect([(pre, ecc, [('outputnode.mask_b0','inputnode.in_mask')])])
    wf.connect([(ecc, sdc, [('outputnode.out_file','inputnode.DWI')])])
    wf.connect([(inputnode, sdc, [('T1_image','inputnode.T1')])])
    wf.connect([(pre, aac, [('outputnode.dwi_b0_merge', 'inputnode.in_dwi')])])
    wf.connect([(hmc, aac, [('outputnode.out_xfms', 'inputnode.in_hmc')])])
    wf.connect([(ecc, aac, [('outputnode.out_xfms', 'inputnode.in_ecc')])])
    wf.connect([(sdc, aac, [('outputnode.out_warp', 'inputnode.in_sdc_syb')])])
    wf.connect([(inputnode, aac, [('T1_image','inputnode.T1')])])
    
    wf.connect([(aac, bias, [('outputnode.out_file','inputnode.in_file')])])
    
    wf.connect([(bias, datasink, [('outputnode.out_file','DWI_hmc_ecc_sdc_bias_corrected')])])
    wf.connect([(hmc, datasink, [('outputnode.out_bvec','out_bvecs')])])
    wf.connect([(pre, datasink, [('outputnode.out_bvals','out_bvals')])])
    wf.connect([(bias, datasink, [('outputnode.b0_mask','b0_mask')])])
    
    return wf




def diffusion_preprocessing_fieldmap_based(datasink_directory, name='diffusion_preprocessing_fieldmap_based'):
    """
    First extract the b0 volumes, co-registration and mean of the b0 volumes.
    See :func:`dwi_utils.b0_dwi_split`, :func:`dwi_utils.b0_flirt_pipeline`, :func:`dwi_utils.b0_average`.

    Then, correct four types of bias from epi : 
     - Head motion correction. See :func:`dwi_corrections.hmc_pipeline`.
     - Susceptibility bias correction. See :func:`dwi_corrections.sdc_fmb`. 
     - Eddy current correction. See :func:`dwi_corrections.ecc_pipeline`.
     - Estimates a single multiplicative bias field from the
    averaged *b0* image and applies it onto the diffusion data set. See :func:`dwi_corrections.remove_bias`.

    Inputnode
    ----------
    in_file : FILE
      Mandatory input. Dwi data set to preprocess.
    in_bvals : FILE
      Mandatory input. Bval file.
    in_bvecs : FILE
      Mandatory input. Bvecs file.
    bmap_mag : FILE
      Mandatory input. Grefield map. Magnitude.
    bmap_pha : FILE
      Mandatory input. Grefield map. Phase.

    Outputnode
    ----------
    out_file : FILE
      Output. The set of b0 volumes.
    out_bvec : FILE
      Output. The bvecs corresponding to the out_dwi.
    out_bval : FILE
      Output. The bvalues corresponding to the out_dwi.
    out_mask : FILE
      Output : The binary mask file.

    """
    from clinica.pipeline.preprocessing.dwi_utils import b0_dwi_split
    from clinica.pipeline.preprocessing.dwi_utils import b0_flirt_pipeline
    from clinica.pipeline.preprocessing.dwi_utils import insert_b0_into_dwi
    from clinica.pipeline.preprocessing.dwi_utils import b0_average
    from clinica.pipeline.preprocessing.dwi_corrections import hmc_pipeline
    from clinica.pipeline.preprocessing.dwi_corrections import sdc_fmb
    from clinica.pipeline.preprocessing.dwi_corrections import ecc_pipeline
    from clinica.pipeline.preprocessing.dwi_corrections import remove_bias
    from nipype.workflows.dmri.fsl.utils import apply_all_corrections
    import nipype.interfaces.fsl as fsl
    import nipype.interfaces.io as nio
    import nipype.interfaces.utility as niu
    import nipype.pipeline.engine as pe
    import os.path as op



    inputnode = pe.Node(niu.IdentityInterface(fields=['in_file', 'in_bvals', 'in_bvecs', 'bmap_mag', 'bmap_pha']), name='inputnode')

    outputnode = pe.Node(niu.IdentityInterface(fields=['out_file', 'out_bvecs', 'out_bvals',  'out_mask']), name='outputnode')

    b0_dwi_split = pe.Node(niu.Function(input_names=['in_file', 'in_bvals', 'in_bvecs'], output_names=['out_b0', 'out_dwi', 'out_bvals', 'out_bvecs'], function=b0_dwi_split), name='b0_dwi_split')

    mask_b0 = pe.Node(fsl.BET(frac=0.3, mask=True, robust=True),
                       name='mask_b0')

    b0_flirt = b0_flirt_pipeline(name='b0_co_registration')            
    b0_avg = pe.Node(niu.Function(input_names=['in_file'], output_names=['out_file'], function=b0_average), name='b0_average')

    insert_b0_into_dwi = pe.Node(niu.Function(input_names=['in_b0', 'in_dwi', 'in_bvals', 'in_bvecs'], output_names=['out_dwi', 'out_bvals', 'out_bvecs'], function=insert_b0_into_dwi), name='insert_b0avg_into_dwi')

    remove_bias_pip = remove_bias(name='remove_bias', datasink_directory=datasink_directory)
    hmc = hmc_pipeline(name='motion_correct', datasink_directory=datasink_directory)
    hmc.inputs.inputnode.ref_num = 0                
    sdc = sdc_fmb(name='fmb_correction', datasink_directory=datasink_directory)
    ecc = ecc_pipeline(name='eddy_correct', datasink_directory=datasink_directory)
    unwarp = apply_all_corrections()

    datasink = pe.Node(nio.DataSink(), name='datasink_preprocessing')
    datasink.inputs.base_directory = op.join(datasink_directory, 'preprocessing/')

    wf = pe.Workflow(name=name)
    wf.connect([
            
            (inputnode,            b0_dwi_split,         [('in_file', 'in_file'),
                                                          ('in_bvals', 'in_bvals'),
                                                          ('in_bvecs', 'in_bvecs')]),
            (b0_dwi_split,         b0_flirt,             [('out_b0', 'inputnode.in_file')]),
            (b0_flirt,             b0_avg,               [('outputnode.out_file', 'in_file')]),
            (b0_avg,               insert_b0_into_dwi,   [('out_file', 'in_b0')]),
            (b0_avg,               mask_b0,              [('out_file', 'in_file')]),
            (b0_dwi_split,         insert_b0_into_dwi,   [('out_dwi', 'in_dwi'),
                                                          ('out_bvals', 'in_bvals'),
                                                          ('out_bvecs', 'in_bvecs')]),
            (insert_b0_into_dwi,   hmc,                  [('out_dwi', 'inputnode.in_file'),
                                                          ('out_bvals', 'inputnode.in_bval'),
                                                          ('out_bvecs', 'inputnode.in_bvec')]),
            (mask_b0,              hmc,                  [('mask_file', 'inputnode.in_mask')]),
            (hmc,                  sdc,                  [('outputnode.out_file', 'inputnode.in_file')]),
            (mask_b0,              sdc,                  [('mask_file', 'inputnode.in_mask')]),
            (inputnode,            sdc,                  [('bmap_mag', 'inputnode.bmap_mag')]),
            (inputnode,            sdc,                  [('bmap_pha', 'inputnode.bmap_pha')]),
            (hmc,                  ecc,                  [('outputnode.out_xfms', 'inputnode.in_xfms')]),
            (insert_b0_into_dwi,   ecc,                  [('out_bvals', 'inputnode.in_bval')]),
            (sdc,                  ecc,                  [('outputnode.out_file', 'inputnode.in_file')]),
            (mask_b0,              ecc,                  [('mask_file', 'inputnode.in_mask')]),
            (insert_b0_into_dwi,   unwarp,               [('out_dwi', 'inputnode.in_dwi')]),
            (hmc,                  unwarp,               [('outputnode.out_xfms', 'inputnode.in_hmc')]),
            (ecc,                  unwarp,               [('outputnode.out_xfms', 'inputnode.in_ecc')]),
            (sdc,                  unwarp,               [('outputnode.out_warp', 'inputnode.in_sdc')]),
            (unwarp,               remove_bias_pip,      [('outputnode.out_file', 'inputnode.in_file')]),
#            (mask_b0,              remove_bias_pip,      [('mask_file', 'inputnode.in_mask')]),
            (hmc,                  outputnode,           [('outputnode.out_bvec', 'out_bvecs')]),
            (hmc,                  datasink,             [('outputnode.out_bvec', 'out_bvecs')]),
            (insert_b0_into_dwi,   outputnode,           [('out_bvals', 'out_bval')]),
            (insert_b0_into_dwi,   datasink,             [('out_bvals', 'out_bval')]),
            (remove_bias_pip,      outputnode,           [('outputnode.out_file', 'out_file')]),
            (remove_bias_pip,      datasink,             [('outputnode.out_file', 'out_file')]),
            (remove_bias_pip,      outputnode,           [('outputnode.b0_mask','b0_mask')]),
            (remove_bias_pip,      datasink,             [('outputnode.b0_mask','b0_mask')])
#            (mask_b0,              outputnode,           [('mask_file', 'out_mask')]),
#            (mask_b0,              datasink,             [('mask_file', 'out_mask')])
            ])

    return wf
