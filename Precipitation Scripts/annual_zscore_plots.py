import xarray as xr
import numpy as np
import zscores_average
import precip_zscores
import glob
import precipAvg_interval as pcp

#Some of this code is a copy-paste from previous Python files (see above - this one is for zscores_average). Since we want all members, that part will be kept.

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
test = zscores_average.phaseMask(zscores, bools)

# Group times by month, then take the mean across members and months. Taking the mean ignores NaNs from the function.
grouped = test.groupby('time.month')
grouped = grouped.mean(dim = ['members', 'time'])

annual = pcp.interval(grouped, months = np.arange(0, 12))
pcp.prettyColors(annual, title = 'Average Annual Z-Scores During PCs', cmap = 'BrBG', save = ('/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Plots/AnnualAvgZscores.png'), clabel = 'Z-Scores')
