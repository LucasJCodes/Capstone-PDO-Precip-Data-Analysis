# Hi yet again. Today we're going to subset the zscores that fall within PDO phase change months and average them together by month.

import xarray as xr
import numpy as np
import precip_zscores
import glob

def phaseMask(zscores, booleans):
    # Zscores is a dataset of the zscores datasets for all members, and pc_months is the list of phase change months.

    # Turn the zeros in the boolean into NaNs.
    pc_months = booleans.where(booleans['is_phase_change'] == 1, drop = False)

    # Multiply the boolean mask onto the zscores so that only zscores during phase change months have values other than NaN.
    modified = zscores * pc_months['is_phase_change']
    return modified

"""  This code is to test the above function to ensure we can get monthly groupings of only phase change precip
data.  Much of this code is used when we create the monthly zscores plots

# Retrieve the precip files, sorted so that each member is in order.
filenames = sorted(glob.glob('/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/PRECTmem*.nc'))

# Calculate the z-scores for each member, then concatenate them with a new "members" dimension.
zscores = [precip_zscores.member_zscore(f) for f in filenames]
zscores = xr.concat(zscores, dim = 'members')

# Read in the booleans that define which months are phase changes.
bools = xr.open_dataset('/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/phaseChanges.nc')
# Rename the month_bool dimension to "time" so that it can be multiplied directly into zscores inside the function.
bools = bools.rename({"month_bool": "time"})

# Run the function.
test = phaseMask(zscores, bools)

# Group times by month, then take the mean across members and months. Taking the mean ignores NaNs from the function.
grouped = test.groupby('time.month')
grouped = grouped.mean(dim = ['members', 'time'])

# Print the result!
print(grouped)
"""