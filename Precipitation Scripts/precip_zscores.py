# Hi again. We're going to make z-scores today. Yay.

import xarray as xr
import numpy as np

# Step 1: Average precip for each month across each member's ~100 years of data.
def member_zscore(dataset):
    # Input 1 will be monthly precip data from one CESM2 member, which has dimensions of lat, lon, and time. Time component will be in months.

    pcp = dataset.groupby('time.month')
    avgs = dataset.groupby('time.month').mean(dim = 'time')
    stds = dataset.groupby('time.month').std(dim = 'time')
    zscores = (pcp - avgs) / stds

    return pcp
    return avgs
    return zscores



    

