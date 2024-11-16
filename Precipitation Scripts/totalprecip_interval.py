'''
In this code, the total precipitation of the averages for certain months (January to March vs June to August) from a single member is calculated.
'''

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

#Convert data into mm/month
def pcp_total(filepath):
    # Input will be the filepath to a netCDF of monthly precip data from one CESM2 member, which has dimensions of lat, lon, and time. Time component will be in months.
    
    dataset = xr.open_dataset(filepath, engine="netcdf4")

    # Grab only the precip portion of the dataset.
    prect = dataset['PRECT']
    # Convert units from m/s to mm/month.
    prect = prect * 3600 * 24 * 30.417 * 1000
   
    # Precip data grouped by month
    pcp = prect.groupby('time.month')

    # Average precipitation for THAT MONTH
    pcp = pcp.mean(dim = 'time')
    # Interval we want
    #CHANGE THIS LINE DEPENDING ON INTERVAL
    interval = pcp.where((pcp.month.isin([6,7,8])), drop = True)
    return interval

#Read in the data
data = pcp_total('C:/Users/17135/Capstone Code/Capstone-PDO-Precip-Data-Analysis/Data/PRECTmem11.nc')

#Sum together the averages
data = data.sum(dim = 'month')

#PLOTTING
#Determine axes and the figure we refer to throughout the code
X, Y = np.meshgrid(data.lon, data.lat)
fig, ax = plt.subplots(nrows = 1, ncols = 1, subplot_kw = {'projection': ccrs.PlateCarree()})
#Fittingly, adds a coastline to the plots
ax.coastlines()
#Adds data and other components
my_ax = ax.contourf(X, Y, data, transform = ccrs.PlateCarree(), cmap = "YlGn")
ax.add_feature(cfeature.STATES, zorder=1, linewidth=1, edgecolor='k')
#CHANGE THIS LINE DEPENDING ON INTERVAL
ax.set_title('Total precipitation using respective averages of Jun-Aug (mm/month)')
fig.colorbar(my_ax, ax = ax)
#save figure
#CHANGE THIS LINE DEPENDING ON INTERVAL
plt.savefig('JuntoAug_SumOfAvgs.png')
