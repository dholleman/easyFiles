# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 13:25:40 2021

@author: Daan Holleman
"""

import numpy as np
import glob, os

def resetDir():
    loc = (os.path.dirname(os.path.realpath(__file__)))
    os.chdir(loc)

def curDir():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path
    print(f'Current Directory: {dir_path}')

def getFileNames(ftype, folder='\\'):
    loc = (os.path.dirname(os.path.realpath(__file__)))
    os.chdir(loc + folder)
    
    fnames = np.array([],dtype=str)
    for file in glob.glob(ftype):
        fnames = np.append(fnames, folder + file)
    
    resetDir()
    return fnames