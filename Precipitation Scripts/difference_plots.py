# The goal of this script is to plot the difference beween precipitation during PDO phase changes and the average precipitation for a given season or for the whole year.

import xarray as xr
import glob
import precipAvg_interval as pcp
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Read in the precip files into one dataset along a new dimension "member"
filenames = sorted(glob.glob('/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/PRECTmem*.nc'))
precip = xr.open_mfdataset(filenames, combine = 'nested', concat_dim = 'members')

# Grab only the precip portion of the dataset and convert units.
prect = precip['PRECT']
prect = prect * 3600 * 24 * 30.417 * 1000
   
# Read in booleans and apply to the precip data so that what's left is only precip during PDO phase changes.
bools = xr.open_dataset('/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/phaseChanges.nc')
bools = bools.rename({"month_bool": "time"})
pc_months = bools.where(bools['is_phase_change'] == 1, drop = False)
modified = prect * pc_months['is_phase_change']

# Group by month and average across months and members.
grouped = modified.groupby('time.month')
pc_precip = grouped.mean(dim = ['members', 'time'])

# Get the average precip across months for ALL months, including non-phase change months.
all_precip = pcp.pcpAvg(filenames)

# Get the difference between average precip for phase change months and average precip for ALL months.
difference = pc_precip - all_precip
print(difference)

annual = pcp.interval(difference, months = np.arange(0, 12))

# Plot the average annual difference.

pcp.prettyColors(annual, title = 'Average Annual PC Precipitation Anomaly (mm)', cmap = 'BrBG', save = '/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Plots/Annual_DifferencePrecip.png', vmin = -75, vmax = 75)

# X, Y = np.meshgrid(annual.lon, annual.lat)
# fig, ax = plt.subplots(nrows = 1, ncols = 1, subplot_kw = {'projection': ccrs.PlateCarree()})
# ax.coastlines()

# my_ax = ax.contourf(X, Y, annual, transform = ccrs.PlateCarree(), cmap = 'BrBG', vmin = -75, 
# vmax = 75)
# ax.add_feature(cfeature.STATES, zorder=1, linewidth=1, edgecolor='k')
# ax.set_title('Average Annual PC Precipitation Anomaly (mm)')
# fig.colorbar(my_ax, ax = ax)
  
# plt.savefig('/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Plots/Annual_DifferencePrecip.png')