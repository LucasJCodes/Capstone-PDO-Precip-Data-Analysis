# Hi again. We're going to make z-scores today. Yay.

import xarray as xr
import numpy as np
import pandas as pd

# Step 1: Average precip for each month across each member's ~100 years of data.
def member_zscore(filepath):
    # Input will be the filepath to a netCDF of monthly precip data from one CESM2 member, which has dimensions of lat, lon, and time. Time component will be in months.
    
    dataset = xr.open_dataset(filepath)

    #print(dataset["PRECT"])

    dataset = dataset['PRECT'] * 3600 * 24 * 30.417 * 1000
   
    # Precip data grouped by month
    pcp = dataset.groupby('time.month')

    # Average and standard deviation for each month's precip (e.g. all Januarys)
    avgs = pcp.mean(dim = 'time')
    stds = pcp.std(dim = 'time')

    # Z-scores calculation
    zscores = (pcp - avgs) / stds
    return zscores
    
mem12 = member_zscore('/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/PRECTmem11.nc')

#print(mem12)

