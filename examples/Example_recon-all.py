#!/usr/bin/python#
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:04:17 2016

@author: Junhao WEN
"""

from __future__ import absolute_import
from clinica.pipeline.preprocessing.t1_freesurfer_workflow import recon_all_pipeline
from os.path import realpath,split,join
import tempfile

data_dir = join(split(realpath(__file__))[0], 'external-data/Recon-all').encode("utf-8")
output_dir = tempfile.mkdtemp()
datasink_para = ['orig', 'white']

print("Data Directory -> %s" % data_dir)
print("Output Directory -> %s" % output_dir)
print("Running...")

# this is to use structureA, grab all the nifti files with the same nams, like 'struct'
def recon_all_exampleA():
    field_templateA = '%s/%s.nii'
    template_argsA =   'struct'
    return recon_all_pipeline(data_dir, output_dir, field_templateA, template_argsA, datasink_para)

# this is to use structureB, grab all the nifti files with different name, like struct1.nii, struct2.nii....   
#def recon_all_exampleB():
#    field_templateB = '%s/struct%d.nii'
#    template_argsB = [['subject_id', 'dir']]
#    #datasink_para is optional, is usend in order to etc...
#    return recon_all_pipeline(data_dir, output_dir, field_templateB, template_argsB, datasink_para)
    
T1_recon_allA = recon_all_exampleA()
T1_recon_allA.run("MultiProc", plugin_args={'n_procs':4})
#T1_recon_allB = recon_all_exampleB()
#T1_recon_allB.run("MultiProc", plugin_args={'n_procs':4})
#T1_recon_all = recon_all_pipeline(data_dir, output_dir, 3)
#T1_recon_all.run("MultiProc", plugin_args={'n_procs':4})