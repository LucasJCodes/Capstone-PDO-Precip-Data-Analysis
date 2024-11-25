'''
This combines our previous codes, "totalprecip_interval.py" and "precip_monthlyAvgs.py", to provide a streamlined process to create plots for one of two scenarios:
    1. An interval of months
    2. Annual
Both take the sum of the average precipitation for the months used, and take in all 10 members.
'''

import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np

def pcpAvg(filepaths):
    # Input will be the filepath to a netCDF of monthly precip data from one CESM2 member, which has dimensions of lat, lon, and time. Time component will be in months.
    
    ds = xr.open_mfdataset(filepaths, combine = 'nested', concat_dim = 'member')

    # Grab only the precip portion of the dataset.
    prect = ds['PRECT']

    # Convert units from m/s to mm/month.
    prect = prect * 3600 * 24 * 30.417 * 1000
   
    # # Precip data grouped by month
    pcp = prect.groupby('time.month')

    # Average for each month's precip (e.g. all Januarys)
    mem_sum = pcp.mean(dim = ['member', 'time'])
    return mem_sum

def interval(data, months):
    interval = data.where((data.month.isin(months)), drop = True)
    interval = interval.sum(dim = 'month')
    return interval

def prettyColors(data, title, cmap, save, **kwargs):
    X, Y = np.meshgrid(data.lon, data.lat)
    fig, ax = plt.subplots(nrows = 1, ncols = 1, subplot_kw = {'projection': ccrs.PlateCarree()})
    ax.coastlines()

    my_ax = ax.contourf(X, Y, data, transform = ccrs.PlateCarree(), cmap = cmap, vmin = kwargs.get('vmin'), vmax = kwargs.get('vmax'))
    ax.add_feature(cfeature.STATES, zorder=1, linewidth=1, edgecolor='k')
    ax.set_title(title)
    fig.colorbar(my_ax, ax = ax)
  
    plt.savefig(save)
