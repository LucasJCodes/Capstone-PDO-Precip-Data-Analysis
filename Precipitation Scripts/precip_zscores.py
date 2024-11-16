# Hi again. We're going to make z-scores today. Yay.

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Step 1: Average precip for each month across each member's ~100 years of data.
def member_zscore(filepath):
    # Input will be the filepath to a netCDF of monthly precip data from one CESM2 member, which has dimensions of lat, lon, and time. Time component will be in months.
    
    #zscores = []
    dataset = xr.open_dataset(filepath)

    #print(dataset["PRECT"])
    prect = dataset['PRECT']
    prect = prect * 3600 * 24 * 30.417 * 1000
   
    # Precip data grouped by month
    pcp = prect.groupby('time.month')
    
    # Average and standard deviation for each month's precip (e.g. all Januarys)
    avgs = pcp.mean(dim = 'time')
    stds = pcp.std(dim = 'time')

    # Z-scores calculation
    anom = pcp - avgs
    zscores = anom.groupby("time.month") / stds
    #print(zscores)
    return zscores

# Now, to check things are going ok, let's plot the zscores on a contour plot. Yay.

data = member_zscore('/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/PRECTmem11.nc')

# Turn cftime dates into something I can deal with.ikl;
data['time'] = data['time'].dt.strftime('%Y%m%d')

# Take the 4D array down to 2D for a specific month and time.
test = data.where((data['time'] == '19840501') & (data.month == 5), drop = True)
test = test.squeeze(('time'), drop = True)

# Plot a contour of zscores for the specific day/month.
#print(test)
X, Y = np.meshgrid(test.lon, test.lat)
fig, ax = plt.subplots(nrows = 1, ncols = 1, subplot_kw = {'projection': ccrs.PlateCarree()})
ax.coastlines()
my_ax = ax.contourf(X, Y, test, transform = ccrs.PlateCarree())
ax.add_feature(cfeature.STATES, zorder=1, linewidth=1, edgecolor='k')
fig.colorbar(my_ax, ax = ax)
plt.show()
