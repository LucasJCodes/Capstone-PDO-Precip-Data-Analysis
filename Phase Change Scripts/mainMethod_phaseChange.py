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
for i in range(11, NUM_FILES + 11):
    temp_ds = xr.open_dataset("Data/SSTmem" + str(i) + ".nc", engine = "netcdf4")

    # The performEOF function has input (ssts) and output (pc1), an xarray dataset with the first principle component of inputted SSTs, or the PDO index.
    # iterate through each of the members to calculate the PDO index for each
    temp_index = performEOF.PDO_index(temp_ds).reset_coords("month", drop = True)

    # The ID_Phase function has inputs (data, period, bound) and output (neutral_dates), a list of months that have been identified as PDO neutral using the rolling average. 
    #data is PDO index values by month.
    #We want the output of performEOF, pc1, to be the data input for ID_phase. So we have to convert pc1 to a Pandas dataframe.

    # Iterate through each of the calculated indices for the different members and find the phase changes
    phaseChanges.append(PDOindex.ID_Phase(temp_index, period = 72, bound = 0.1)[0])
    
#write all the data to a file
"""
dataset1 = xr.open_dataset("Data/SSTmem11.nc")
index = performEOF.PDO_index(dataset1).reset_coords("month", drop = True)
changes = PDOindex.ID_Phase(index, period = 72, bound = 0.1)[0]
"""

print(phaseChanges)

data_array = xr.DataArray(
    phaseChanges,
    dims=["members", "month_bool"],
    name="is_phase_change"
)

final = data_array.to_dataset()

print(final)

#final["members"] = final["members"].to_datetimeindex()

final.to_netcdf("/Users/lucas/source/repos/Capstone-PDO-Precip-Data-Analysis/Data/phaseChanges.nc")