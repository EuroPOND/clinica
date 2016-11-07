#!/usr/bin/python#
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:04:17 2016

@author: Junhao WEN
"""

from __future__ import absolute_import
from clinica.pipeline.t1.t1_freesurfer import recon_all_pipeline
from os.path import realpath,split,join
import time
import tempfile

# Test for BIDS dataset(which is located in dataARAMIS/users/CLINICA/CLINICA_datasets/for_testing, you should adjust the input path here on your own computer)
# this example is run on my own Mac, so this path should be changed if you run on your own machine.
data_dir_CAPP = '/Volumes/dataARAMIS/users/CLINICA/CLINICA_datasets/for_testing/CAPP_BIDStesting'
output_dir = tempfile.mkdtemp()
# output_dir = '/Volumes/dataARAMIS/users/CLINICA/CLINICA_datasets/for_testing/test_surfstat'
tsv_file_CAPP = '/Volumes/dataARAMIS/users/CLINICA/CLINICA_datasets/for_testing/subjects_visits_list_CAPP.tsv'
#
# data_dir_INSIGHT = '/Volumes/dataARAMIS/users/CLINICA/CLINICA_datasets/for_testing/INSIGHT_BIDStesting'
# tsv_file_INSIGHT = '/Volumes/dataARAMIS/users/CLINICA/CLINICA_datasets/for_testing/subjects_visits_list_INSIGHT.tsv'

# test in home
# data_dir_CAPP = '/Users/junhao.wen/test/test-reconall-home'
# output_dir = '/Users/junhao.wen/test/test-reconall-home-result'
# tsv_file_CAPP = '/Users/junhao.wen/test/test-reconall-home/subjects_visits_list_CAPP.tsv'
analysis_series_id = 'default'
start = time.time()

# this is the example to run CAPP dataset
def recon_all_example_CAPP():
    return recon_all_pipeline(data_dir_CAPP, output_dir, tsv_file_CAPP, analysis_series_id)

# # this is the example to run INSIGHT dataset
# def recon_all_example_INSIGHT():
#     return recon_all_pipeline(data_dir_INSIGHT, output_dir,tsv_file_INSIGHT)

if 2 > 1:
    print("Data Directory -> %s" % data_dir_CAPP)
    print("Output Directory -> %s" % output_dir)
    print("Running...")
    T1_recon_all = recon_all_example_CAPP()
    T1_recon_all.run("MultiProc", plugin_args={'n_procs':4})
    time_consuming = time.time() - start
    print 'END! time consuming is : %s' % time_consuming
else:
    print("Data Directory -> %s" % data_dir_INSIGHT)
    print("Output Directory -> %s" % output_dir)
    print("Running...")
    T1_recon_all = recon_all_example_INSIGHT()
    T1_recon_all.run("MultiProc", plugin_args={'n_procs':4})
    time_consuming = time.time() - start
    print 'END! time consuming is : %s' % time_consuming

# command line example:
# clinica run t1-freesurfer /Volumes/dataARAMIS/users/CLINICA/CLINICA_datasets/BIDS/PREVDEMALS_BIDS/GENFI ~/test/test-reconall-lab/ /Volumes/dataARAMIS/users/junhao.wen/PhD/PREVDEMALS/Freesurfer/Reconall/reconall_GENFI/subjects_visits_list_PREVDEMALS.tsv 'default'