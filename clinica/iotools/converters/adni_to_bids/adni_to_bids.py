
from clinica.iotools.abstract_converter import Converter
from clinica.engine.cmdparser import CmdParser
import logging

__author__ = "Sabrina Fontanella"
__copyright__ = "Copyright 2017, The Aramis Lab Team"
__credits__ = ["Jorge Samper"]
__license__ = ""
__version__ = "0.1.0"
__maintainer__ = "Sabrina Fontanella"
__email__ = "sabrina.fontanella@icm-institute.org"
__status__ = "Development"


class AdniToBids(Converter):

    def get_modalities_supported(self):
        return ['T1', 'PET_FDG', 'PET_AV45']

    def convert_clinical_data(self,  clinical_data_dir, out_path):
        """
        Convert the clinical data of ADNI specified into the file clinical_specifications_adni.xlsx

        :param clinical_data_dir: path to the clinical data directory
        :param out_path: path to the BIDS directory
        """
        from os import path
        import os
        import logging
        import clinica.iotools.bids_utils as bids
        import pandas as pd
        from glob import glob
        from os.path import normpath
        import clinica.iotools.converters.adni_to_bids.adni_utils as adni_utils

        clinic_specs_path = path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data',
                                      'clinical_specifications_adni.xlsx')
        try:
            os.path.exists(out_path)
        except IOError:
            print 'BIDS folder not found.'
            raise

        bids_ids = bids.get_bids_subjs_list(out_path)
        bids_subjs_paths = bids.get_bids_subjs_paths(out_path)

        # -- Creation of participant.tsv --
        logging.info("--Creating sessions files. --")
        participants_df = bids.create_participants_df('ADNI', clinic_specs_path, clinical_data_dir, bids_ids)

        # Replace the original values with the standard defined by the AramisTeam
        participants_df['sex'] = participants_df['sex'].replace('Male', 'M')
        participants_df['sex'] = participants_df['sex'].replace('Female', 'F')

        participants_df.to_csv(path.join(out_path, 'participants.tsv'), sep='\t', index=False)

        # -- Creation of sessions.tsv --
        logging.info("--Creating of sessions files. --")
        print("\nCreation of sessions files...")
        adni_utils.create_adni_sessions_dict(bids_ids, clinic_specs_path, clinical_data_dir, bids_subjs_paths)

        # -- Creation of scans files --
        print 'Creating of scans files...'
        adni_utils.create_adni_scans_files(clinic_specs_path, bids_subjs_paths, bids_ids)

    def convert_images(self, source_dir, clinical_dir, dest_dir, subjs_list_path='', mod_to_add=''):
        '''

        :param source_dir: path to the ADNI dataset directory
        :param clinical_dir: path to the clinical data directory
        :param dest_dir: path to the BIDS directory
        :param subjs_list_path: list of subjects to process
        :param mod_to_add:
        :param mod_to_update:
        :return:
        '''

        import os
        from os import path
        import pandas as pd
        import adni_modalities.adni_t1 as adni_t1
        import adni_modalities.adni_av45_pet as adni_av45
        import adni_modalities.adni_fdg_pet as adni_fdg

        adni_merge_path = path.join(clinical_dir, 'ADNIMERGE.csv')
        adni_merge = pd.read_csv(adni_merge_path)
        paths_files_location = path.join(dest_dir, 'conversion_info')

        print subjs_list_path

        # Load a file with subjects list or compute all the subjects
        if subjs_list_path is not None and subjs_list_path!='':
            subjs_list = [line.rstrip('\n') for line in open(subjs_list_path)]
        else:
            print 'Using all the subjects contained into ADNI merge...'
            subjs_list = adni_merge['PTID'].unique()

        # Create the output folder if is not already existing
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            os.makedirs(path.join(dest_dir, 'conversion_info'))

        if mod_to_add == 'T1' or not mod_to_add:
            print 'Calculating paths for T1. Output will be in ', paths_files_location
            t1_paths = adni_t1.compute_t1_paths(source_dir, clinical_dir, dest_dir, subjs_list)
            print 'Done!'
            adni_t1.t1_paths_to_bids(t1_paths, dest_dir, dcm2niix="dcm2niix", dcm2nii="dcm2nii", mod_to_update=True)

        if mod_to_add=='PET_FDG' or not mod_to_add :
            print 'Calculating paths for PET_FDG. Output will be in ', paths_files_location
            pet_fdg_paths = adni_fdg.compute_fdg_pet_paths(source_dir, clinical_dir, dest_dir, subjs_list)
            print 'Done!'
            adni_fdg.convert_adni_fdg_pet(source_dir, clinical_dir, dest_dir, subjs_list)

        if mod_to_add == 'PET_AV45' or not mod_to_add:
            print 'Calculating paths for PET_FDG. Output will be in ', paths_files_location
            pet_av45_paths = adni_av45.compute_av45_pet_paths(source_dir, clinical_dir, dest_dir, subjs_list)
            print 'Done!'
            adni_av45.convert_adni_av45_pet(source_dir, clinical_dir, dest_dir, subjs_list)