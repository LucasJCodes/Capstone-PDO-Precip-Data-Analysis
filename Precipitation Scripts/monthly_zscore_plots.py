'''
This code will plot the average z-scores for a specific month
We need the monthly plots of z-scores during phase changes

Good codes to look at: 
    zscores_average (precip z-scores for phase change months)
    precip_zscores (has a plot looking at a particular month, though will need to change based on what the original meant to plot)
'''

import xarray as xr
import numpy as np
import zscores_average
import precip_zscores
import glob
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

#Some of this code is a copy-paste from previous Python files (see above - this one is for zscores_average). Since we want all members, that part will be kept.

# Retrieve the precip files, sorted so that each member is in order.
filenames = sorted(glob.glob('Data/PRECTmem*.nc'))

# Calculate the z-scores for each member, then concatenate them with a new "members" dimension.
zscores = [precip_zscores.member_zscore(f) for f in filenames]
zscores = xr.concat(zscores, dim = 'members')

# Read in the booleans that define which months are phase changes.
bools = xr.open_dataset('Data/phaseChanges.nc')
# Rename the month_bool dimension to "time" so that it can be multiplied directly into zscores inside the function.
bools = bools.rename({"month_bool": "time"})

# Run the function.
test = zscores_average.phaseMask(zscores, bools)

# Group times by month, then take the mean across members and months. Taking the mean ignores NaNs from the function.
grouped = test.groupby('time.month')
grouped = grouped.mean(dim = ['members', 'time'])

# Print the result!
#print(grouped)

#PLOTTING CONTOUR MAPS (this part is somewhat new?)

# Might need these line, but let's see first
# data['time'] = data['time'].dt.strftime('%Y%m%d')

# Choose which month to plot
selected_by_month = grouped.where((grouped.month == 1), drop = True)
selected_by_month = selected_by_month.squeeze(('month'), drop = True)
print(selected_by_month)

#Plot the selected month
X, Y = np.meshgrid(selected_by_month.lon, selected_by_month.lat)
fig, ax = plt.subplots(nrows = 1, ncols = 1, subplot_kw = {'projection': ccrs.PlateCarree()})
ax.coastlines()
my_ax = ax.contourf(X, Y, selected_by_month, transform = ccrs.PlateCarree())
ax.add_feature(cfeature.STATES, zorder=1, linewidth=1, edgecolor='k')
fig.colorbar(my_ax, ax = ax)
plt.show()