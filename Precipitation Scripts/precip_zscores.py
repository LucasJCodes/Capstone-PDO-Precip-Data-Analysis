# Hi again. We're going to make z-scores today. Yay.

import xarray as xr
import numpy as np

# Step 1: Average precip for each month across each member's ~100 years of data.
def member_zscore(dataset):
    # Input will be monthly precip data from one CESM2 member, which has dimensions of lat, lon, and time. Time component will be in months.

    # Precip data grouped by month
    pcp = dataset.groupby('time.month')
    # Average precip for each month (e.g. all Januarys)
    avgs = dataset.groupby('time.month').mean(dim = 'time')

    # Standard deviation for each individual month
    stds = dataset.std(dim = 'time')
    zscores = (pcp - avgs) / stds

    return pcp, avgs, zscores
    



    

