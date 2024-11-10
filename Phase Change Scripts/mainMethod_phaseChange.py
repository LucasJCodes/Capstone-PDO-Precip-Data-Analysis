# Hi. How are you? Hope you're doing well. Today we are going to make a function that puts all of our fancy EOF and PDO functions together. Enjoy :)

import xarray as xr
from eofs.xarray import Eof
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import performEOF
import PDOindex

NUM_FILES = 10
files = []
index_list = []
phaseChanges = []

#read in all the files using a for loop to add them to the files list
for file in range(11, NUM_FILES + 11):
    temp_ds = xr.open_dataset("Data/SSTmem" + str(file) + ".nc", engine = "netcdf4")
    files.append(temp_ds)


# The performEOF function has input (ssts) and output (pc1), an xarray dataset with the first principle component of inputted SSTs, or the PDO index.
# iterate through each of the members to calculate the PDO index for each
for file in files:
    index_list.append(performEOF.PDO_index(file))

# The ID_Phase function has inputs (data, period, bound) and output (neutral_dates), a list of months that have been identified as PDO neutral using the rolling average. 
#data is PDO index values by month.
#We want the output of performEOF, pc1, to be the data input for ID_phase. So we have to convert pc1 to a Pandas dataframe.

# Iterate through each of the calculated indices for the different members and find the phase changes
for member in index_list:
    curr_index = member.to_dataframe()
    phaseChanges.append(PDOindex.ID_Phase(curr_index, period = 36, bound = 0.5))

print("here")

