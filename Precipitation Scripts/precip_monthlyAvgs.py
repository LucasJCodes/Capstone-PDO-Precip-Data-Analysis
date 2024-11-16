# This is a script that will calculate the average precipitation for each month at each gridpoint from CESM2 model data.

import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np

def pcp_monthlyAvg(filepath):
    # Input will be the filepath to a netCDF of monthly precip data from one CESM2 member, which has dimensions of lat, lon, and time. Time component will be in months.
    
    ds = xr.open_mfdataset(filepath, combine = 'nested', concat_dim = 'member')

    # Grab only the precip portion of the dataset.
    prect = ds['PRECT']

    # Convert units from m/s to mm/month.
    prect = prect * 3600 * 24 * 30.417 * 1000
   
    # # Precip data grouped by month
    pcp = prect.groupby('time.month')

    # Average for each month's precip (e.g. all Januarys)
    mem_sum = pcp.mean(dim = ['member', 'time'])
    avg = mem_sum.sum(dim = 'month')
    #avg = mem_sum.mean(dim = 'month')

    #annual_sum = pcp.sum(dim = 'member').groupby('time.month')
    #annual_avg = annual_sum.mean(dim = 'month')
    return avg

test = pcp_monthlyAvg(filepath = '/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/PRECTmem*.nc')

# tot = test.where(test.month == 8, drop = True)
# tot = jun.squeeze(('month'), drop = True)

X, Y = np.meshgrid(test.lon, test.lat)
fig, ax = plt.subplots(nrows = 1, ncols = 1, subplot_kw = {'projection': ccrs.PlateCarree()})
ax.coastlines()
my_ax = ax.contourf(X, Y, test, transform = ccrs.PlateCarree())
ax.add_feature(cfeature.STATES, zorder=1, linewidth=1, edgecolor='k')
fig.colorbar(my_ax, ax = ax)
plt.savefig('avgAnnual_allMembers.png')