# coding: utf8

import clinica.engine as ce

__author__ = "Jorge Samper Gonzalez"
__copyright__ = "Copyright 2016-2018, The Aramis Lab Team"
__credits__ = ["Jorge Samper Gonzalez"]
__license__ = "See LICENSE.txt file"
__version__ = "0.1.0"
__maintainer__ = "Jorge Samper Gonzalez"
__email__ = "jorge.samper-gonzalez@inria.fr"
__status__ = "Development"


class PETVolumeCLI(ce.CmdParser):

    def define_name(self):
        """Define the sub-command name to run this pipelines.
        """
        self._name = 'pet-volume'

    def define_description(self):
        """Define a description of this pipeline.
        """
        self._description = 'SPM-based pre-processing of PET images:\nhttp://clinica.run/doc/Pipelines/PET_Volume/'

    def define_options(self):
        """Define the sub-command arguments
        """

        self._args.add_argument("bids_directory",
                                help='Path to the BIDS directory.')
        self._args.add_argument("caps_directory",
                                help='Path to the CAPS directory.')
        self._args.add_argument("group_id",
                                help='User-defined identifier for the provided group of subjects.')
        self._args.add_argument("-tsv", "--subjects_sessions_tsv",
                                help='TSV file containing the subjects with their sessions.')
        self._args.add_argument("-fwhm", "--fwhm_tsv",
                                help='TSV file containing the fwhm_x, fwhm_y and fwhm_z for each pet image.')
        self._args.add_argument("-pet_type", "--pet_type", type=str, default='fdg', choices=['fdg', 'av45'],
                                help='PET image type. Possible values are fdg and av45.')
        self._args.add_argument("-mask", "--mask_tissues", nargs='+', type=int, default=[1, 2, 3], choices=range(1, 7),
                                help="Tissue classes (gray matter, GM; white matter, WM; cerebro-spinal fluid, CSF...) to use for masking the PET image. Ex: 1 2 3 is GM, WM and CSF")
        self._args.add_argument("-threshold", "--mask_threshold", type=float, default=0.3,
                                help='Value to be used as threshold to binarize the tissues mask.')
        self._args.add_argument("-pvc_mask", "--pvc_mask_tissues", nargs='+', type=int, default=[1, 2, 3], choices=range(1, 7),
                                help="Tissue classes (gray matter, GM; white matter, WM; cerebro-spinal fluid, CSF...) to use as mask for PVC. Ex: 1 2 3 is GM, WM and CSF")
        self._args.add_argument("-smooth", "--smooth", nargs='+', type=int, default=[8],
                                help="A list of integers specifying the different isomorphic fwhm in milimeters to smooth the image")
        self._args.add_argument("-atlases", "--atlases", nargs='+', type=str,
                                default=['AAL2', 'LPBA40', 'Neuromorphometrics', 'AICHA', 'Hammers'],
                                choices=['AAL2', 'LPBA40', 'Neuromorphometrics', 'AICHA', 'Hammers'],
                                help='A list of atlases to use to calculate the mean GM concentration at each region')
        self._args.add_argument("-wd", "--working_directory",
                                help='Temporary directory to store pipelines intermediate results')
        self._args.add_argument("-np", "--n_procs", type=int,
                                help='Number of cores used to run in parallel')
        self._args.add_argument("-sl", "--slurm", action='store_true',
                                help='Run the pipelines using SLURM')

    def run_command(self, args):
        """
        """

        from pet_volume_pipeline import PETVolume

        pipeline = PETVolume(bids_directory=self.absolute_path(args.bids_directory),
                                       caps_directory=self.absolute_path(args.caps_directory),
                                       tsv_file=self.absolute_path(args.subjects_sessions_tsv),
                                       group_id=args.group_id,
                                       fwhm_tsv=self.absolute_path(args.fwhm_tsv)
                                       )

        pipeline.parameters.update({'pet_type': args.pet_type,
                                    'mask_tissues': args.mask_tissues,
                                    'mask_threshold': args.mask_threshold,
                                    'pvc_mask_tissues': args.pvc_mask_tissues,
                                    'smooth': args.smooth,
                                    'atlas_list': args.atlases
                                    })

        pipeline.base_dir = self.absolute_path(args.working_directory)

        if args.n_procs:
            pipeline.run(plugin='MultiProc', plugin_args={'n_procs': args.n_procs})
        elif args.slurm:
            pipeline.run(plugin='SLURM')
        else:
            pipeline.run()
