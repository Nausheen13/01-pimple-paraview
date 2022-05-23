from multiprocessing.sharedctypes import Value
import sys
import PyFoam
import os
import scipy
import math
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timezone
import paraview

from os import path
from distutils.dir_util import copy_tree
from PyFoam.RunDictionary.SolutionDirectory import SolutionDirectory
from PyFoam.RunDictionary.ParsedParameterFile import ParsedParameterFile
from PyFoam.Basics.DataStructures import Vector
from PyFoam.Execution.ConvergenceRunner import ConvergenceRunner
from PyFoam.LogAnalysis.BoundingLogAnalyzer import BoundingLogAnalyzer
from PyFoam.Execution.AnalyzedRunner import AnalyzedRunner
from PyFoam.LogAnalysis.SimpleLineAnalyzer import GeneralSimpleLineAnalyzer
from PyFoam.Execution.UtilityRunner import UtilityRunner

from PyFoam.Applications.PVSnapshot import PVSnapshot
from PyFoam.Execution.BasicRunner import BasicRunner

import pandas as pd
import numpy as np
from scipy.signal import find_peaks

from numpy import linspace

Newcase = "pimple"
run = BasicRunner(
     argv=["pimpleFoam", "-case", Newcase], logname="Solution",
)
run.start()

Snapshot= PVSnapshot(args=["--state=pimple1.pvsm","--latest-time",Newcase])

