def PDO_index(ssts):
    """
    This function computes the Pacific Decadal Oscillation index from a xarray dataset of 
    sea surface temperatures in the North Pacific from 110E to 100W and 20N to 70N and 
    outputs it as an xarray dataset.

    To do this, the function weights SSTs at each grid point by grid area and then uses the 
    eofs package [Dawson 2016] to calculate the  empirical orthogonal function (EOF) 
    of the SST data.  The resulting first principle component is the PDO index.

    Authors: 
        Lucas Jones in collaboration with Brianna DeFore, Daniel Fenske, Roy Galang

    Args:
        ssts (dataset): an xarray data set of raw SSTs over the 110E to 100W and 20N to 70N region 
              defining the PDO. 

    Returns:
        pc1 (dataset): An xarray data set holding the first principle component of the inputted SSTs

    Dawson A. eofs: A Library for EOF Analysis of Meteorological, Oceanographic, and Climate Data. 
    *Journal of Open Research Software*. 2016;4(1):e14. doi:10.5334/jors.122
    """

    import xarray as xr
    from eofs.xarray import Eof
    import numpy as np

    #remove the trend  of the data to exclude any possible changes due to climate change
    regress = ssts.polyfit(dim = "time", deg = 1)  #calculate regression

    fit = xr.polyval(ssts["time"], regress.SST_polyfit_coefficients)

    detrended = ssts - fit

    #take the time mean for each month and hold it in a data set 
    monthly_clim = detrended.groupby("time.month").mean(dim = "time")

    #use the time mean and original data to calulate the anomaly for each month
    month_anoms = (detrended.groupby("time.month") - monthly_clim).to_dataarray()

    #weight the data based on grid cell area by taking the square root of the cosine of latitude
    #store weightings in a numpy array
    weights = np.sqrt(np.cos(np.deg2rad(month_anoms["lat"].values)))[:, np.newaxis]

    #create and EOF solver object in eofs class
    calc_eof = Eof(month_anoms[0], weights = weights)

    #get the 1st principle component (PC1)
    pc1 = calc_eof.pcs(npcs = 1, pcscaling = 1)

    #output PC1
    return pc1



#testing of the function
import xarray as xr
import matplotlib.pyplot as plt
from PDOindex import ID_Phase

data = xr.open_dataset("Data/SSTmem15.nc")

index = PDO_index(data)

"""
plt.figure()
index[:, 0].plot(color = "blue")
ax = plt.gca()
ax.axhline(0, color = "black")

ax.set_xlabel("Years")
ax.set_ylabel("Normalized Units")

ax.set_ylim(-4, 4)
ax.set_title("PC1: The Index Timeseries")
"""

bound = 0.1
mon_length = 72

neutral = ID_Phase(index, mon_length, bound)

index = index.to_dataset()
dates = index["time"].to_index().to_datetimeindex()

print(dates)

index['Color'] = ['red' if pcs > bound else 'blue' if pcs < -bound else 'black' for pcs in index["pcs"]]

fig,ax = plt.subplots(figsize=(15,4))
ax.bar(dates, index['pcs'], width=45) #color = index['Color'])

fig2,ax2 = plt.subplots(figsize=(15,4))
ax2.step(index['Date'], index['Phase Change'])
ax2.set_ylim(0,2)
ax2.set_yticks([0,1,2])

plt.savefig("index.png")
