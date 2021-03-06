# coding: utf8


"""This module contains FreeSurfer utilities."""


def freesurfer_volume_to_native_volume(
        freesurfer_volume,
        native_volume,
        name_output_volume=None):
    """
    Convert FreeSurfer volume in native space.

    This function converts any volume in FreeSurfer's conformed space
    (1x1x1mm voxel size, 256x256x256 dimension) into a volume in native space.

    For further details:
    https://surfer.nmr.mgh.harvard.edu/fswiki/FsAnat-to-NativeAnat

    Args:
        freesurfer_volume (str): Volume in FreeSurfer's conformed space
            (e.g. aparc+aseg.mgz containing the Desikan parcellation)
        native_volume (str): Volume in native space (You should choose
            ${SUBJECTS_DIR}/subject_id/mri/rawavg.mgz).
        name_output_volume (Optional[str]): Name of the output matrix
            (default=volume_in_native_space.nii.gz).

    Returns:
        out_volume (str): volume in native space (the file is saved here:
            ${SUBJECTS_DIR}/subject_id/native_space/label.nii)

    Example:
        >>> from clinica.utils.freesurfer import freesurfer_volume_to_native_volume
        >>> freesurfer_volume_to_native_volume(bert/mri/rawavg.mgz, bert/mri/aparc+aseg.mgz, 'aparc-in-native-space.nii')
    """
    import os
    import os.path as op

    assert(op.isfile(freesurfer_volume))
    assert(op.isfile(native_volume))

    if name_output_volume is None:
        out_volume = op.abspath('volume_in_native_space.nii.gz')
    else:
        out_volume = op.abspath(name_output_volume)

    cmd = 'mri_vol2vol --regheader --no-save-reg --mov %s --targ %s --o %s' \
          % (freesurfer_volume, native_volume, out_volume)
    os.system(cmd)

    return out_volume


def fs_caps2reconall(caps_dir, dest_dir, subjects_visits_tsv):
    """
        This function is to transfer caps recon-all output structure to standard FreeSurfer recon-all output structure.

    Args:
        caps_dir: CAPS directory containing the outputs in CAPS hierarchy
        dest_dir: the destination folder containing the FreeSurfer output structure
        subjects_visits_tsv: tsv files containing the subjects that you want to convert

    Returns:

    """
    import os, csv
    from shutil import copytree

    subject_list = []
    session_list = []
    with open(subjects_visits_tsv, 'rb') as tsvin:
        tsv_reader = csv.reader(tsvin, delimiter='\t')

        for row in tsv_reader:
            if row[0] == 'participant_id':
                continue
            else:
                subject_list.append(row[0])
                session_list.append(row[1])

    output_path = os.path.expanduser(caps_dir)  # change the relative path to be absolute path
    caps_dir = os.path.join(output_path, 'subjects')

    for i in range(len(subject_list)):
        if os.path.isdir(os.path.join(dest_dir, subject_list[i] + '_' + session_list[i])):
            print "This subject: %s for FreeSurfer exits already!" % subject_list[i]
        else:
            print "Convert subject: %s from CAPS to FreeSurfer output structure" % subject_list[i]
            copytree(os.path.join(caps_dir, subject_list[i], session_list[i], 't1/freesurfer_cross_sectional', subject_list[i] + '_' + session_list[i]), os.path.join(dest_dir, subject_list[i] + '_' + session_list[i]))
            print "--------------Finish this subject!-----------------------"


def volumetric_summary(subject_dir, subject_id, caps_dir):
    """
        To write statistics summary for all the subjects after reconall pipelines.

    Args:
        subject_dir: a list containing all the CAPS directory path
        subject_id: a list containing all the participant_id
        caps_dir: destination folder containing the summarized statistics tsv

    Returns:

    """
    import os, errno

    # name all the 26 tsv output files.
    all_seg_volume = '_parcellation-wm_volume.tsv'
    aseg_volume = '_segmentationVolumes.tsv'

    aparc_desikan_lh_volume = '_hemi-left_parcellation-desikan_volume.tsv'
    aparc_desikan_rh_volume = '_hemi-right_parcellation-desikan_volume.tsv'
    aparc_desikan_lh_thickness = '_hemi-left_parcellation-desikan_thickness.tsv'
    aparc_desikan_rh_thickness = '_hemi-right_parcellation-desikan_thickness.tsv'
    aparc_desikan_lh_area = '_hemi-left_parcellation-desikan_area.tsv'
    aparc_desikan_rh_area = '_hemi-right_parcellation-desikan_area.tsv'
    aparc_desikan_lh_meancurv = '_hemi-left_parcellation-desikan_meancurv.tsv'
    aparc_desikan_rh_meancurv = '_hemi-right_parcellation-desikan_meancurv.tsv'

    aparc_destrieux_lh_volume = '_hemi-left_parcellation-destrieux_volume.tsv'
    aparc_destrieux_rh_volume = '_hemi-right_parcellation-destrieux_volume.tsv'
    aparc_destrieux_lh_thickness = '_hemi-left_parcellation-destrieux_thickness.tsv'
    aparc_destrieux_rh_thickness = '_hemi-right_parcellation-destrieux_thickness.tsv'
    aparc_destrieux_lh_area = '_hemi-left_parcellation-destrieux_area.tsv'
    aparc_destrieux_rh_area = '_hemi-right_parcellation-destrieux_area.tsv'
    aparc_destrieux_lh_meancurv = '_hemi-left_parcellation-destrieux_meancurv.tsv'
    aparc_destrieux_rh_meancurv = '_hemi-right_parcellation-destrieux_meancurv.tsv'

    aparc_BA_lh_volume = '_hemi-left_parcellation-ba_volume.tsv'
    aparc_BA_rh_volume = '_hemi-right_parcellation-ba_volume.tsv'
    aparc_BA_lh_thickness = '_hemi-left_parcellation-ba_thickness.tsv'
    aparc_BA_rh_thickness = '_hemi-right_parcellation-ba_thickness.tsv'
    aparc_BA_lh_area = '_hemi-left_parcellation-ba_area.tsv'
    aparc_BA_rh_area = '_hemi-right_parcellation-ba_area.tsv'
    aparc_BA_lh_meancurv = '_hemi-left_parcellation-ba_meancurv.tsv'
    aparc_BA_rh_meancurv = '_hemi-right_parcellation-ba_meancurv.tsv'

    dest_dir = os.path.join(caps_dir, 'subjects', 'regional_measures_summary')
    try:
        os.makedirs(dest_dir)
    except OSError as exception:
        if exception.errno != errno.EEXIST: # if dest_dir exists, go on, if its other error, raise
            raise

    # fetch the paths for all the 26 tsv files.
    all_seg_volume_tsv = os.path.join(dest_dir, all_seg_volume)
    aseg_volume_tsv = os.path.join(dest_dir, aseg_volume)
    # DESIKAN atlas(?h.aparc.stats)
    aparc_desikan_lh_volume_tsv = os.path.join(dest_dir, aparc_desikan_lh_volume)
    aparc_desikan_rh_volume_tsv = os.path.join(dest_dir, aparc_desikan_rh_volume)
    aparc_desikan_lh_thickness_tsv = os.path.join(dest_dir, aparc_desikan_lh_thickness)
    aparc_desikan_rh_thickness_tsv = os.path.join(dest_dir, aparc_desikan_rh_thickness)
    aparc_desikan_lh_area_tsv = os.path.join(dest_dir, aparc_desikan_lh_area)
    aparc_desikan_rh_area_tsv = os.path.join(dest_dir, aparc_desikan_rh_area)
    aparc_desikan_lh_meancurv_tsv = os.path.join(dest_dir, aparc_desikan_lh_meancurv)
    aparc_desikan_rh_meancurv_tsv = os.path.join(dest_dir, aparc_desikan_rh_meancurv)
    # DESTRIEUX atals
    aparc_destrieux_lh_volume_tsv = os.path.join(dest_dir, aparc_destrieux_lh_volume)
    aparc_destrieux_rh_volume_tsv = os.path.join(dest_dir, aparc_destrieux_rh_volume)
    aparc_destrieux_lh_thickness_tsv = os.path.join(dest_dir, aparc_destrieux_lh_thickness)
    aparc_destrieux_rh_thickness_tsv = os.path.join(dest_dir, aparc_destrieux_rh_thickness)
    aparc_destrieux_lh_area_tsv = os.path.join(dest_dir, aparc_destrieux_lh_area)
    aparc_destrieux_rh_area_tsv = os.path.join(dest_dir, aparc_destrieux_rh_area)
    aparc_destrieux_lh_meancurv_tsv = os.path.join(dest_dir, aparc_destrieux_lh_meancurv)
    aparc_destrieux_rh_meancurv_tsv = os.path.join(dest_dir, aparc_destrieux_rh_meancurv)
    # Brodmann Area atlas
    aparc_BA_lh_volume_tsv = os.path.join(dest_dir, aparc_BA_lh_volume)
    aparc_BA_rh_volume_tsv = os.path.join(dest_dir, aparc_BA_rh_volume)
    aparc_BA_lh_thickness_tsv = os.path.join(dest_dir, aparc_BA_lh_thickness)
    aparc_BA_rh_thickness_tsv = os.path.join(dest_dir, aparc_BA_rh_thickness)
    aparc_BA_lh_area_tsv = os.path.join(dest_dir, aparc_BA_lh_area)
    aparc_BA_rh_area_tsv = os.path.join(dest_dir, aparc_BA_rh_area)
    aparc_BA_lh_meancurv_tsv = os.path.join(dest_dir, aparc_BA_lh_meancurv)
    aparc_BA_rh_meancurv_tsv = os.path.join(dest_dir, aparc_BA_rh_meancurv)

    # get the cmd string for the command line wrappers
    subjects = ''
    for i in xrange(len(subject_dir)):
        subject_path = (os.path.join(subject_dir[i], subject_id[i]))
        subjects += subject_path + ' '

    cmd_all_seg = 'asegstats2table --subjects ' + subjects + '--meas volume --statsfile wmparc.stats --all-seg --tablefile ' + all_seg_volume_tsv
    os.system(cmd_all_seg)
    cmd_aseg = 'asegstats2table --subjects ' + subjects + '--meas volume --tablefile ' + aseg_volume_tsv
    os.system(cmd_aseg)

    cmd_aparc_desikan_lh_volume = 'aparcstats2table --subjects ' + subjects + '--hemi lh --meas volume --tablefile ' + aparc_desikan_lh_volume_tsv
    os.system(cmd_aparc_desikan_lh_volume)
    cmd_aparc_desikan_rh_volume = 'aparcstats2table --subjects ' + subjects + '--hemi rh --meas volume --tablefile ' + aparc_desikan_rh_volume_tsv
    os.system(cmd_aparc_desikan_rh_volume)
    cmd_parc_desikan_lh_thickness = 'aparcstats2table --subjects ' + subjects + '--hemi lh --meas thickness --tablefile ' + aparc_desikan_lh_thickness_tsv
    os.system(cmd_parc_desikan_lh_thickness)
    cmd_parc_desikan_rh_thickness = 'aparcstats2table --subjects ' + subjects + '--hemi rh --meas thickness --tablefile ' + aparc_desikan_rh_thickness_tsv
    os.system(cmd_parc_desikan_rh_thickness)
    cmd_aparc_desikan_lh_area = 'aparcstats2table --subjects ' + subjects + '--hemi lh --meas area --tablefile ' + aparc_desikan_lh_area_tsv
    os.system(cmd_aparc_desikan_lh_area)
    cmd_aparc_desikan_rh_area = 'aparcstats2table --subjects ' + subjects + '--hemi rh --meas area --tablefile ' + aparc_desikan_rh_area_tsv
    os.system(cmd_aparc_desikan_rh_area)
    cmd_aparc_desikan_lh_meancurv = 'aparcstats2table --subjects ' + subjects + '--hemi lh --meas meancurv --tablefile ' + aparc_desikan_lh_meancurv_tsv
    os.system(cmd_aparc_desikan_lh_meancurv)
    cmd_aparc_desikan_rh_meancurv = 'aparcstats2table --subjects ' + subjects + '--hemi rh --meas meancurv --tablefile ' + aparc_desikan_rh_meancurv_tsv
    os.system(cmd_aparc_desikan_rh_meancurv)

    cmd_aparc_destrieux_lh_volume = 'aparcstats2table --subjects ' + subjects + '--hemi lh --parc aparc.a2009s --meas volume --tablefile ' + aparc_destrieux_lh_volume_tsv
    os.system(cmd_aparc_destrieux_lh_volume)
    cmd_aparc_destrieux_rh_volume = 'aparcstats2table --subjects ' + subjects + '--hemi rh --parc aparc.a2009s --meas volume --tablefile ' + aparc_destrieux_rh_volume_tsv
    os.system(cmd_aparc_destrieux_rh_volume)
    cmd_parc_destrieux_lh_thickness = 'aparcstats2table --subjects ' + subjects + '--hemi lh --parc aparc.a2009s --meas thickness --tablefile ' + aparc_destrieux_lh_thickness_tsv
    os.system(cmd_parc_destrieux_lh_thickness)
    cmd_parc_destrieux_rh_thickness = 'aparcstats2table --subjects ' + subjects + '--hemi rh --parc aparc.a2009s --meas thickness --tablefile ' + aparc_destrieux_rh_thickness_tsv
    os.system(cmd_parc_destrieux_rh_thickness)
    cmd_aparc_destrieux_lh_area = 'aparcstats2table --subjects ' + subjects + '--hemi lh --parc aparc.a2009s --meas area --tablefile ' + aparc_destrieux_lh_area_tsv
    os.system(cmd_aparc_destrieux_lh_area)
    cmd_aparc_destrieux_rh_area = 'aparcstats2table --subjects ' + subjects + '--hemi rh --parc aparc.a2009s --meas area --tablefile ' + aparc_destrieux_rh_area_tsv
    os.system(cmd_aparc_destrieux_rh_area)
    cmd_aparc_destrieux_lh_meancurv = 'aparcstats2table --subjects ' + subjects + '--hemi lh --parc aparc.a2009s --meas meancurv --tablefile ' + aparc_destrieux_lh_meancurv_tsv
    os.system(cmd_aparc_destrieux_lh_meancurv)
    cmd_aparc_destrieux_rh_meancurv = 'aparcstats2table --subjects ' + subjects + '--hemi rh --parc aparc.a2009s --meas meancurv --tablefile ' + aparc_destrieux_rh_meancurv_tsv
    os.system(cmd_aparc_destrieux_rh_meancurv)

    #### BA atals does not work for FreeSurfer 6.0
    # cmd_aparc_BA_lh_volume = 'aparcstats2table --subjects ' + subjects + '--hemi lh --parc BA --meas volume --tablefile ' + aparc_BA_lh_volume_tsv
    # os.system(cmd_aparc_BA_lh_volume)
    # cmd_aparc_BA_rh_volume = 'aparcstats2table --subjects ' + subjects + '--hemi rh --parc BA --meas volume --tablefile ' + aparc_BA_rh_volume_tsv
    # os.system(cmd_aparc_BA_rh_volume)
    # cmd_parc_BA_lh_thickness = 'aparcstats2table --subjects ' + subjects + '--hemi lh --parc BA --meas thickness --tablefile ' + aparc_BA_lh_thickness_tsv
    # os.system(cmd_parc_BA_lh_thickness)
    # cmd_parc_BA_rh_thickness = 'aparcstats2table --subjects ' + subjects + '--hemi rh --parc BA --meas thickness --tablefile ' + aparc_BA_rh_thickness_tsv
    # os.system(cmd_parc_BA_rh_thickness)
    # cmd_aparc_BA_lh_area = 'aparcstats2table --subjects ' + subjects + '--hemi lh --parc BA --meas area --tablefile ' + aparc_BA_lh_area_tsv
    # os.system(cmd_aparc_BA_lh_area)
    # cmd_aparc_BA_rh_area = 'aparcstats2table --subjects ' + subjects + '--hemi rh --parc BA --meas area --tablefile ' + aparc_BA_rh_area_tsv
    # os.system(cmd_aparc_BA_rh_area)
    # cmd_aparc_BA_lh_meancurv = 'aparcstats2table --subjects ' + subjects + '--hemi lh --parc BA --meas meancurv --tablefile ' + aparc_BA_lh_meancurv_tsv
    # os.system(cmd_aparc_BA_lh_meancurv)
    # cmd_aparc_BA_rh_meancurv = 'aparcstats2table --subjects ' + subjects + '--hemi rh --parc BA --meas meancurv --tablefile ' + aparc_BA_rh_meancurv_tsv
    # os.system(cmd_aparc_BA_rh_meancurv)


def write_volumetric_summary(caps_dir, subjects_visits_tsv):
    """
        This func is to write the volumetric measurement after recon-all pipelines for all the subjects

    Args:
        caps_dir:
        subjects_visits_tsv: tsv contains all the particiapnt_id and session_id

    Returns:

    """
    ### TODO, this should be done after we define the name of the tsv file for each subject, otherwise this will be changed often....
    #### NOT USE

    import nipype.pipeline.engine as pe
    from nipype.interfaces.utility import Function
    import pandas as pd
    import os

    # get the list for subject_ids
    subjects_visits = pd.io.parsers.read_csv(subjects_visits_tsv, sep='\t')
    if (list(subjects_visits.columns.values)[0] != 'participant_id') and (list(subjects_visits.columns.values)[1] != 'session_id'):
        raise Exception('Subjects and visits file is not in the correct format.')
    subject_list = list(subjects_visits.participant_id)
    session_list = list(subjects_visits.session_id)
    subject_id = list(subject_list[i] + '_' + session_list[i] for i in range(len(subject_list)))
    subject_dir = []
    for i in xrange(len(subject_id)):
        sub_dir = os.path.join(caps_dir, 'subjects', subject_list[i], session_list[i], 't1', 'freesurfer_cross_sectional')
        subject_dir.append(sub_dir)


    fs_tsv_summary = pe.Node(name='volumetric_summary_node',
                            interface=Function(
                                input_names=['subject_dir', 'subject_id', 'caps_dir'],
                                output_names=[],
                                function=volumetric_summary))
    fs_tsv_summary.inputs.subject_id = subject_id
    fs_tsv_summary.inputs.caps_dir = caps_dir
    fs_tsv_summary.inputs.subject_dir = subject_dir

    return fs_tsv_summary


def write_volumetric_per_subject(caps_dir, subjects_visits_tsv):
    """
        This func is to write the volumetric measurement after recon-all pipelines for each subjects in the subjects_visits_tsv

    Args:
        caps_dir: CAPS directory
        subjects_visits_tsv: tsv contains all the particiapnt_id and session_id

    Returns:

    """
    import nipype.pipeline.engine as pe
    from nipype.interfaces.utility import Function
    import pandas as pd
    from clinica.pipelines.t1_freesurfer_cross_sectional.t1_freesurfer_cross_sectional_utils import write_statistics_per_subject

    # get the list for subject_ids
    subjects_visits = pd.io.parsers.read_csv(subjects_visits_tsv, sep='\t')
    if (list(subjects_visits.columns.values)[0] != 'participant_id') and (list(subjects_visits.columns.values)[1] != 'session_id'):
        raise Exception('Subjects and visits file is not in the correct format.')
    subject_list = list(subjects_visits.participant_id)
    session_list = list(subjects_visits.session_id)
    subject_id = list(subject_list[i] + '_' + session_list[i] for i in range(len(subject_list)))

    fs_tsv_subject = pe.MapNode(name='volumetric_summary_node',
                                iterfield=['subject_id'],
                                interface=Function(
                                input_names=['subject_id', 'output_dir'],
                                output_names=[],
                                function=write_statistics_per_subject,
                                imports=['import os', 'import errno']))
    fs_tsv_subject.inputs.subject_id = subject_id
    fs_tsv_subject.inputs.output_dir = caps_dir

    return fs_tsv_subject


def write_reconall_log_summary(caps_dir, subjects_visits_tsv):
    """
        This func is to write the recon_all.log summary for all the subjects, the first step quality check

    Args:
        caps_dir: CAPS directory
        subjects_visits_tsv: tsv contains all the particiapnt_id and session_id

    Returns:

    """
    import nipype.pipeline.engine as pe
    from nipype.interfaces.utility import Function
    import pandas as pd
    from clinica.pipelines.t1_freesurfer_cross_sectional.t1_freesurfer_cross_sectional_utils import log_summary

    # get the list for subject_ids
    subjects_visits = pd.io.parsers.read_csv(subjects_visits_tsv, sep='\t')
    if (list(subjects_visits.columns.values)[0] != 'participant_id') and (
        list(subjects_visits.columns.values)[1] != 'session_id'):
        raise Exception('Subjects and visits file is not in the correct format.')
    subject_list = list(subjects_visits.participant_id)
    session_list = list(subjects_visits.session_id)
    subject_id = list(subject_list[i] + '_' + session_list[i] for i in range(len(subject_list)))

    lognode = pe.Node(name='lognode',
                      interface=Function(
                          input_names=['subject_list', 'session_list', 'subject_id', 'output_dir'],
                          output_names=[],
                          function=log_summary))
    lognode.inputs.subject_list = subject_list
    lognode.inputs.session_list = session_list
    lognode.inputs.subject_id = subject_id
    lognode.inputs.output_dir = caps_dir

    return lognode


