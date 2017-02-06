#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module contains pipelines for the processing of DWI dataset."""


def dwi_processing_pipeline(
        subject_id, session_id, caps_directory,
        analysis_series_id='default', working_directory=None,
        atlas_name=None,
        max_harmonic_order=None, tractography_algorithm='iFOD2', tractography_nb_of_tracks="100K",
        tractography_fod_threshold=None, tractography_step_size=None, tractography_angle=None,
        nthreads=2, name="whole_brain_tractography_pipeline"):
    """
    Process corrected DWI dataset.

    This pipeline is the main DWI processing pipeline combining these different pipeline:
        - (Single-shell) tractography, DTI & DTI-scalar measures pipeline
        - DTI-based analysis pipeline

    .. warning :: This is not suited for multi-shell data at all.

    Args:
        subject_id (str): Subject ID in a BIDS format ('sub-<participant_label>').
        session_id (str): Session ID in a BIDS format ('ses-<session_label>').
        analysis_series_id (str): Analysis series ID (will create the 'analysis-series-<analysis_series_id>/' folder
            for the CAPS hierarchy)
        caps_directory (str): Directory where the results are stored in a CAPS hierarchy.
        working_directory (Optional[str]): Directory where the temporary results are stored. If not specified, it is
            automatically generated (generally in /tmp/).
        max_harmonic_order (Optional[int]): See dti_and_tractography_pipeline::max_harmonic_order
        tractography_algorithm (Optional[str]): See dti_and_tractography_pipeline::tractography_algorithm
        tractography_nb_of_tracks (Optional[str]): See dti_and_tractography_pipeline::tractography_nb_of_tracks
        tractography_fod_threshold (Optional[float]): See dti_and_tractography_pipeline::tractography_fod_threshold
        tractography_step_size (Optional[int]): See dti_and_tractography_pipeline::tractography_step_size
        tractography_angle (Optional[int]): See dti_and_tractography_pipeline::tractography_angle
        nthreads (Optional[int]): Number of threads used for the pipeline (default=2, 0 disables multi-threading).
        name (Optional[str]): Name of the pipeline.

    Inputnode:
        in_dwi_nii (str): File containing DWI dataset in NIfTI format.
        in_bvals (str): File containing B-Value table in FSL format.
        in_bvecs (str): File containing Diffusion Gradient table in FSL format.
        in_b0_mask (str): Binary mask of the b0 image. Only perform computation within this specified binary brain mask image.
        in_white_matter_binary_mask (str): Binary mask of the white matter segmentation. Seed streamlines will be
            entirely generated at random within this mask.

    Outputnode:

    Example:
        >>> from clinica.pipeline.dwi.dwi_processing import dwi_processing_pipeline
        >>> dwi_processing= dwi_processing_pipeline(subject_id='sub-CLNC01', session_id='ses-M00', caps_directory='/path/to/output/folder')
        >>> dwi_processing.run()
    """
    import tempfile
    import nipype.interfaces.io as nio
    import nipype.interfaces.utility as niu
    import nipype.pipeline.engine as pe
    from clinica.pipeline.dwi.dwi_processing import tractography_and_dti_pipeline
    from clinica.pipeline.dwi.dwi_white_matter_scalar_analysis import dti_based_analysis_pipeline
    from clinica.utils.check_dependency import check_ants, check_mrtrix


    check_ants(); check_mrtrix()

    if working_directory is None:
        working_directory = tempfile.mkdtemp()

    inputnode = pe.Node(niu.IdentityInterface(
        fields=['in_dwi_nii', 'in_bvecs', 'in_bvals', 'in_b0_mask', 'in_white_matter_binary_mask']),
        name='inputnode')

    tractography_and_dti = tractography_and_dti_pipeline(
        subject_id=subject_id, session_id=session_id, caps_directory=caps_directory,
        analysis_series_id=analysis_series_id, working_directory=working_directory,
        max_harmonic_order=max_harmonic_order, tractography_algorithm=tractography_algorithm,
        tractography_nb_of_tracks=tractography_nb_of_tracks, tractography_fod_threshold=tractography_fod_threshold,
        tractography_step_size=tractography_step_size, tractography_angle=tractography_angle,
        nthreads=nthreads)

    dti_based_analysis = dti_based_analysis_pipeline(
        subject_id=subject_id, session_id=session_id, caps_directory=caps_directory,
        analysis_series_id=analysis_series_id, working_directory=None, atlas_name=atlas_name)


    outputnode = pe.Node(niu.IdentityInterface(
        fields=['out_dwi_mif', 'out_dti', 'out_metrics', 'out_fa', 'out_md', 'out_ad', 'out_rd', 'out_ev',
                'out_response_function', 'out_sh_coefficients_image', 'out_tracks']),
        name='outputnode')

    datasink = pe.Node(nio.DataSink(), name='datasink')
    datasink.inputs.base_directory = caps_directory

    wf = pe.Workflow(name=name, base_dir=working_directory)
    wf.connect([
        (inputnode, tractography_and_dti, [('in_dwi_nii', 'inputnode.in_dwi_nii'),
                                           ('in_bvals', 'inputnode.in_bvals'),
                                           ('in_bvecs', 'inputnode.in_bvecs'),
                                           ('in_b0_mask', 'inputnode.in_b0_mask'),
                                           ('in_white_matter_binary_mask', 'inputnode.in_white_matter_binary_mask')]),
        (tractography_and_dti,dti_based_analysis , [('outputnode.out_fa', 'inputnode.in_fa'),
                                                    ('outputnode.out_md', 'inputnode.in_md'),
                                                    ('outputnode.out_ad', 'inputnode.in_ad'),
                                                    ('outputnode.out_rd', 'inputnode.in_rd')]),
        # Outputnode:
        (tractography_and_dti, outputnode, [('outputnode.out_dwi_mif', 'out_dwi_mif'),
                                            ('outputnode.out_dti', 'out_dti'),
                                            ('outputnode.out_fa', 'out_fa'),
                                            ('outputnode.out_md', 'out_md'),
                                            ('outputnode.out_rd', 'out_rd'),
                                            ('outputnode.out_ev', 'out_ev'),
                                            ('outputnode.out_eroded_mask', 'out_eroded_mask'),
                                            ('outputnode.out_response_function', 'out_response_function'),
                                            ('outputnode.out_sh_coefficients_image', 'out_sh_coefficients_image'),
                                            ('outputnode.out_tracks', 'out_tracks')])
    ])

    return wf



def tractography_and_dti_pipeline(
        subject_id, session_id, caps_directory,
        analysis_series_id = 'default', working_directory=None,
        max_harmonic_order=None, tractography_algorithm='iFOD2', tractography_nb_of_tracks="100K",
        tractography_fod_threshold=None, tractography_step_size=None, tractography_angle=None,
        nthreads=2, name="tractography_and_dti_pipeline"):
    """
    Perform single-shell tractography and DTI.

    This pipeline performs a whole-brain single-shell tractography and DTI on a preprocessed DWI dataset. This Python
    implementation is using MRtrix3 and is based on the tutorial given by the MRtrix community during the ISMRM
    conference in 2015.

    .. warning :: This is not suited for multi-shell data at all.

    Args:
        subject_id (str): Subject ID in a BIDS format ('sub-<participant_label>').
        session_id (str): Session ID in a BIDS format ('ses-<session_label>').
        analysis_series_id (str): Analysis series ID (will create the 'analysis-series-<analysis_series_id>/' folder
            for the CAPS hierarchy)
        caps_directory (str): Directory where the results are stored in a CAPS hierarchy.
        working_directory (Optional[str]): Directory where the temporary results are stored. If not specified, it is
            automatically generated (generally in /tmp/).
        max_harmonic_order (Optional[int]): Maximum harmonic order according to the b-vectors
        tractography_algorithm (Optional[str]): See streamlines_tractography
        tractography_nb_of_tracks (Optional[str]): See streamlines_tractography
        tractography_fod_threshold (Optional[float]): See streamlines_tractography
        tractography_step_size (Optional[int]): See streamlines_tractography
        tractography_angle (Optional[int]): See streamlines_tractography
        nthreads (Optional[int]): Number of threads used for the pipeline (default=2, 0 disables multi-threading).
        name (Optional[str]): Name of the pipeline.

    Inputnode:
        in_dwi_nii (str): File containing DWI dataset in NIfTI format.
        in_bvals (str): File containing B-Value table in FSL format.
        in_bvecs (str): File containing Diffusion Gradient table in FSL format.
        in_b0_mask (str): Binary mask of the b0 image. Only perform computation within this specified binary brain mask image.
        in_white_matter_binary_mask (str): Binary mask of the white matter segmentation. Seed streamlines will be
            entirely generated at random within this mask.

    Outputnode:
        out_dwi_mif (str): Preprocessed DWI in MRtrix format.
        out_dti (str): Tensor fitted to the DWI dataset.
        out_metrics (str): Maps of tensor-derived parameters namely fractional anisotropy, mean diffusivity (also
            called mean apparent diffusion), radial diffusivity and the first eigenvector modulated by the FA.
        out_eroded_mask (str): Eroded b0 mask (for debug purposes)
        out_response_function (str): Text file containing response function coefficients.
        out_sh_coefficients_image (str): File containing the spherical harmonics coefficients image
        out_tracks (str): File containing the generated tracks.

    Example:
        >>> from clinica.pipeline.dwi.dwi_processing import tractography_and_dti_pipeline
        >>> tractography_and_dti = tractography_and_dti_pipeline(subject_id='sub-CLNC01', session_id='ses-M00', caps_directory='/path/to/output/folder')
        >>> tractography_and_dti.inputs.inputnode.in_dwi = 'subject_dwi.nii'
        >>> tractography_and_dti.inputs.inputnode.in_bvecs = 'subject_dwi.bvecs'
        >>> tractography_and_dti.inputs.inputnode.in_bvals = 'subject_dwi.bvals'
        >>> tractography_and_dti.inputs.inputnode.in_b0_mask = 'subject_b0_mask.nii'
        >>> tractography_and_dti.inputs.inputnode.white_matter_mask = 'subject_wm_mask.nii'
        >>> tractography_and_dti.run()
    """
    from os.path import join
    import tempfile
    import nipype.interfaces.io as nio
    import nipype.interfaces.utility as niu
    import nipype.pipeline.engine as pe
    from clinica.pipeline.dwi.dwi_processing_utils import convert_nifti_to_mrtrix_format
    from clinica.pipeline.dwi.dwi_processing_utils import dwi_to_tensor
    from clinica.pipeline.dwi.dwi_processing_utils import tensor_to_metrics
    from clinica.pipeline.dwi.dwi_processing_utils import erode_mask
    from clinica.pipeline.dwi.dwi_processing_utils import estimate_response
    from clinica.pipeline.dwi.dwi_processing_utils import estimate_fod
    from clinica.pipeline.dwi.dwi_processing_utils import streamlines_tractography
    from clinica.utils.check_dependency import check_mrtrix

    check_mrtrix()

    if working_directory is None:
        working_directory = tempfile.mkdtemp()

    inputnode = pe.Node(niu.IdentityInterface(
        fields=['in_dwi_nii', 'in_bvecs', 'in_bvals', 'in_b0_mask', 'in_white_matter_binary_mask']),
        name='inputnode')

    convert_nifti_to_mrtrix_format = pe.Node(interface=niu.Function(
        input_names=['in_dwi_nii', 'in_bvals', 'in_bvecs', 'nthreads'],
        output_names=['out_dwi_mif'],
        function=convert_nifti_to_mrtrix_format), name='convert_nifti_to_mrtrix_format')
    convert_nifti_to_mrtrix_format.inputs.nthreads = nthreads

    dwi_to_tensor = pe.Node(interface=niu.Function(
        input_names=['in_dwi_mif', 'in_b0_mask', 'nthreads'],
        output_names=['out_dti'],
        function=dwi_to_tensor), name='dwi_to_tensor')
    dwi_to_tensor.inputs.nthreads = nthreads

    tensor_to_metrics = pe.Node(interface=niu.Function(
        input_names=['in_dti', 'in_b0_mask', 'nthreads'],
        output_names=['out_fa', 'out_md', 'out_ad', 'out_rd', 'out_ev'],
        function=tensor_to_metrics), name='tensor_to_metrics')

    erode_mask = pe.Node(interface=niu.Function(
        input_names=['in_mask', 'npass', 'nthreads'],
        output_names=['out_eroded_mask'], function=erode_mask), name='erode_mask')
    erode_mask.inputs.nthreads = nthreads

    estimate_response = pe.Node(interface=niu.Function(
        input_names=['in_dwi_mif', 'in_b0_mask', 'lmax', 'algorithm', 'tmpdir', 'nthreads'],
        output_names=['out_response_function'], function=estimate_response), name='estimate_response')
    estimate_response.inputs.lmax = max_harmonic_order
    estimate_response.inputs.tmpdir = working_directory
    estimate_response.inputs.nthreads = nthreads

    estimate_fod = pe.Node(interface=niu.Function(
        input_names=['in_dwi_mif', 'in_b0_mask', 'in_response_function_coefficients', 'lmax', 'nthreads'],
        output_names=['out_sh_coefficients_image'], function=estimate_fod), name='estimate_fod')
    estimate_fod.inputs.lmax = max_harmonic_order
    estimate_fod.inputs.nthreads = nthreads

    streamlines_tractography = pe.Node(interface=niu.Function(
        input_names=['in_source', 'in_white_matter_binary_mask', 'algorithm', 'number_of_tracks',
                     'fod_threshold', 'step_size', 'angle', 'nthreads'],
        output_names=['out_tracks'], function=streamlines_tractography), name='streamlines_tractography')
    streamlines_tractography.inputs.algorithm = tractography_algorithm
    streamlines_tractography.inputs.number_of_tracks = tractography_nb_of_tracks
    streamlines_tractography.inputs.fod_threshold = tractography_fod_threshold
    streamlines_tractography.inputs.step_size = tractography_step_size
    streamlines_tractography.inputs.angle = tractography_angle
    streamlines_tractography.inputs.nthreads = nthreads

    outputnode = pe.Node(niu.IdentityInterface(
        fields=['out_dwi_mif', 'out_dti', 'out_metrics', 'out_fa', 'out_md', 'out_ad', 'out_rd', 'out_ev',
                'out_eroded_mask', 'out_response_function', 'out_sh_coefficients_image', 'out_tracks']),
        name='outputnode')

    datasink = pe.Node(nio.DataSink(), name='datasink')
    caps_identifier = subject_id + '_' + session_id
    datasink.inputs.base_directory = join(
        caps_directory, 'analysis-series-' + analysis_series_id, 'subjects', subject_id, session_id, 'dwi')
    datasink.inputs.substitutions = [('dti.mif', caps_identifier + '_dti.mif'),
                                     ('dwi.mif', caps_identifier + '_dwi.mif'),
                                     ('eroded_mask.nii.gz', caps_identifier + '_eroded-b0-mask.nii.gz'),
                                     ('dec_fa_map_from_dti.nii.gz', caps_identifier + '_dec-fa-map-from-dti.nii.gz'),
                                     ('fa_map_from_dti.nii.gz', caps_identifier + '_fa-map-from-dti.nii.gz'),
                                     ('md_map_from_dti.nii.gz', caps_identifier + '_md-map-from-dti.nii.gz'),
                                     ('ad_map_from_dti.nii.gz', caps_identifier + '_ad-map-from-dti.nii.gz'),
                                     ('rd_map_from_dti.nii.gz', caps_identifier + '_rd-map-from-dti.nii.gz'),
                                     ('out_response_function_tax.txt', caps_identifier + '_response-function.txt'),
                                     ('out_response_function_', caps_identifier + '_response-function_algo-'),
                                     ('sh_coefficients_image.mif', caps_identifier + '_sh-coefficients-image.mif'),
                                     ('out_tracks_', caps_identifier + '_fibers-')
                                     ]

    wf = pe.Workflow(name=name)
    wf.connect([
        # Conversion to MRtrix format:
        (inputnode, convert_nifti_to_mrtrix_format, [('in_dwi_nii', 'in_dwi_nii'),
                                                     ('in_bvals', 'in_bvals'),
                                                     ('in_bvecs', 'in_bvecs')]),
        # Computation of the DTI:
        (inputnode,                      dwi_to_tensor, [('in_b0_mask', 'in_b0_mask')]),
        (convert_nifti_to_mrtrix_format, dwi_to_tensor, [('out_dwi_mif', 'in_dwi_mif')]),
        # Computation of the different metrics from the DTI:
        (inputnode,     tensor_to_metrics, [('in_b0_mask', 'in_b0_mask')]),
        (dwi_to_tensor, tensor_to_metrics, [('out_dti', 'in_dti')]),
        # Erosion of the b0 mask for the estimation of the response function:
        (inputnode, erode_mask, [('in_b0_mask', 'in_mask')]),
        # Estimation of the response function:
        (convert_nifti_to_mrtrix_format, estimate_response, [('out_dwi_mif', 'in_dwi_mif')]),
        (erode_mask,                     estimate_response, [('out_eroded_mask', 'in_b0_mask')]),
        # Estimation of the FOD using CSD:
        (convert_nifti_to_mrtrix_format, estimate_fod, [('out_dwi_mif', 'in_dwi_mif')]),
        (inputnode,                      estimate_fod, [('in_b0_mask', 'in_b0_mask')]),
        (estimate_response,              estimate_fod, [('out_response_function', 'in_response_function_coefficients')]),
        # Whole-brain tractography:
        (estimate_fod, streamlines_tractography, [('out_sh_coefficients_image', 'in_source')]),
        (inputnode,    streamlines_tractography, [('in_white_matter_binary_mask', 'in_white_matter_binary_mask')]),
        # Outputnode:
        (convert_nifti_to_mrtrix_format, outputnode, [('out_dwi_mif', 'out_dwi_mif')]),
        (dwi_to_tensor,                  outputnode, [('out_dti', 'out_dti')]),
        (tensor_to_metrics,              outputnode, [('out_fa', 'out_fa'),
                                                      ('out_md', 'out_md'),
                                                      ('out_ad', 'out_ad'),
                                                      ('out_rd', 'out_rd'),
                                                      ('out_ev', 'out_ev')]),
        (erode_mask,                     outputnode, [('out_eroded_mask', 'out_eroded_mask')]),
        (estimate_response,              outputnode, [('out_response_function', 'out_response_function')]),
        (estimate_fod,                   outputnode, [('out_sh_coefficients_image', 'out_sh_coefficients_image')]),
        (streamlines_tractography,       outputnode, [('out_tracks', 'out_tracks')]),
        # Saving files with datasink:
        (convert_nifti_to_mrtrix_format, datasink, [('out_dwi_mif', 'mrtrix.@dwi_mif')]),
        (dwi_to_tensor,                  datasink, [('out_dti', 'mrtrix.@dti')]),
        (tensor_to_metrics,              datasink, [('out_fa', 'mrtrix.@metrics.@fa'),
                                                    ('out_ad', 'mrtrix.@metrics.@ad'),
                                                    ('out_md', 'mrtrix.@metrics.@md'),
                                                    ('out_rd', 'mrtrix.@metrics.@rd'),
                                                    ('out_ev', 'mrtrix.@metrics.@ev')]),
        (erode_mask,                     datasink, [('out_eroded_mask', 'mrtrix.@eroded_mask')]),
        (estimate_response,              datasink, [('out_response_function', 'mrtrix.@response_function')]),
        (estimate_fod,                   datasink, [('out_sh_coefficients_image', 'mrtrix.@sh_coefficients_image')]),
        (streamlines_tractography,       datasink, [('out_tracks', 'mrtrix.@tracks')])
    ])

    return wf



