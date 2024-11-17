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

def interval(filepaths, months):
    data = pcpAvg(filepaths)
    interval = data.where((data.month.isin(months)), drop = True)
    interval = interval.sum(dim = 'month')
    return interval

def prettyColors(data, title, cmap):
    #PLOTTING
    #Determine axes and the figure we refer to throughout the code
    X, Y = np.meshgrid(data.lon, data.lat)
    fig, ax = plt.subplots(nrows = 1, ncols = 1, subplot_kw = {'projection': ccrs.PlateCarree()})
    #Fittingly, adds a coastline to the plots
    ax.coastlines()
    #Adds data and other components
    my_ax = ax.contourf(X, Y, data, transform = ccrs.PlateCarree(), cmap = cmap)
    ax.add_feature(cfeature.STATES, zorder=1, linewidth=1, edgecolor='k')
    #CHANGE THIS LINE DEPENDING ON INTERVAL
    ax.set_title(title)
    fig.colorbar(my_ax, ax = ax)
    #save figure
    #CHANGE THIS LINE DEPENDING ON INTERVAL
    plt.show()

#Monthly interval
roy = interval(filepaths = '/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/PRECTmem*.nc', months = [6, 7, 8])
prettyColors(data = roy, title = 'Average Summertime Precipitation (mm)', cmap = 'YlGn')

#Annual interval
daniel = interval(filepaths = '/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/PRECTmem*.nc', months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
prettyColors(data = daniel, title = 'Average Annual Precipitation (mm)', cmap = 'YlGn')