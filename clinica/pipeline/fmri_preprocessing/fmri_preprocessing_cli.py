"""fMRI Preprocessing - Clinica Command Line Interface.
This file has been generated automatically by the `clinica generate template`
command line tool. See here for more details: https://gitlab.icm-institute.org/aramis/clinica/wikis/docs/InteractingWithClinica.
"""


import clinica.engine as ce

class fMRIPreprocessingCLI(ce.CmdParser):
    """
    """

    def define_name(self):
        """Define the sub-command name to run this pipeline.
        """

        self._name = 'fmri-preprocessing'


    def define_options(self):
        """Define the sub-command arguments
        """

        self._args.add_argument("bids_directory",
                                help='Path to the BIDS directory')
        self._args.add_argument("caps_directory",
                                help='Path to the CAPS directory')
        self._args.add_argument("-tsv", "--subjects_sessions_tsv",
                                help='TSV file containing the subjects with their sessions')
        self._args.add_argument("-wd", "--working_directory",
                                help='Temporary directory to store pipeline intermediate results')
        self._args.add_argument("-np", "--n_procs", type=int,
                                help='Number of processors to run in parallel')
        self._args.add_argument("-sl", "--slurm", action='store_true',
                                help='Run the pipeline using SLURM')
        self._args.add_argument("-ns", "--num_slices", type=int,
                                help="Number of slices")
        self._args.add_argument("-tr", "--time_repetition", type=float,
                                help='TR in seconds')
        self._args.add_argument("-et", "--echo_times", nargs=2, type=float,
                                help="Echo times in seconds (ex.: '-et 5.19 7.65')")
        self._args.add_argument("-bd", "--blip_direction", type=int,
                                help="Blip direction (1 or -1)")
        self._args.add_argument("-fwhm", "--full_width_at_half_maximum",
                                nargs=3, type=int, default=[8, 8, 8],
                                help="Size of the fwhm filter in milimeters to smooth the image")
        self._args.add_argument("-trt", "--total_readout_time", type=float,
                                help="Total readout time (TRT) in seconds")
        self._args.add_argument("-t1s", "--t1_native_space", action='store_true',
                                help="Also return images in T1 native space")
        self._args.add_argument("-fsbm", "--freesurfer_brain_mask",
                                action='store_true',
                                help="Use Freesurfer's pre-computed brain mask")
        self._args.add_argument("-u", "--unwarping",
                                action='store_true',
                                help="Add SPM's Unwarping to the Realign step")


    def run_pipeline(self, args):
        """
        """

        from fmri_preprocessing_pipeline import fMRIPreprocessing

        pipeline = fMRIPreprocessing(bids_directory=self.absolute_path(args.bids_directory),
                                     caps_directory=self.absolute_path(args.caps_directory),
                                     tsv_file=self.absolute_path(args.subjects_sessions_tsv))
        pipeline.parameters = {
            'num_slices'                 : args.num_slices,
            'time_repetition'            : args.time_repetition,
            'echo_times'                 : args.echo_times,
            'blip_direction'             : args.blip_direction,
            'total_readout_time'         : args.total_readout_time,
            'full_width_at_half_maximum' : args.full_width_at_half_maximum,
            't1_native_space'            : args.t1_native_space,
            'freesurfer_brain_mask'      : args.freesurfer_brain_mask,
            'unwarping'                  : args.unwarping
        }
        pipeline.base_dir = self.absolute_path(args.working_directory)
        if args.n_procs:
            pipeline.run(plugin='MultiProc', plugin_args={'n_procs': args.n_procs})
        elif args.slurm:
            pipeline.run(plugin='SLURMGraph', plugin_args = {
                'dont_resubmit_completed_jobs': True, 'sbatch_args': '--qos=short'})
        else:
            pipeline.run()