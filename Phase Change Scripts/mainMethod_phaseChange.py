# Hi. How are you? Hope you're doing well. Today we are going to make a function that puts all of our fancy EOF and PDO functions together. Enjoy :)

import xarray as xr
from eofs.xarray import Eof
from eofs.examples import example_data_path  #for testing purposes
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import pandas as pd
import performEOF
import PDOindex

# The first input is the subsetted SST netCDF data from Roy's computer.

# The performEOF function has input (ssts) and output (pc1), an xarray dataset with the first principle component of inputted SSTs, or the PDO index.
pc1 = performEOF.performEOF(subsetted_SST)

# The ID_Phase function has inputs (data, period, bound) and output (neutral_dates), a list of months that have been identified as PDO neutral using the rolling average. 
    #data is PDO index values by month.
    #We want the output of performEOF, pc1, to be the data input for ID_phase. So ID_phase must be able to import an xarray.
    
neutral = PDOindex.ID_Phase(pc1, period = 36, bound = 0.5)

"""
Note: This function will not work as written because pc1 is an xarray and ID_Phase takes in a CSV file. Need to make performEOF output compatible with ID_Phase, or vice versa.
"""