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
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
from PDOindex import ID_Phase


bound = 0.1
period = 72

data_in = xr.open_dataset("Data/SSTmem11.nc")

index = PDO_index(data_in)

index = index.to_dataset()
squeezed = index.squeeze(dim = "mode")

neutral, dates = ID_Phase(squeezed["pcs"], period, bound)

#Since the plot wants to use datetime formats, we need to convert cftime into datetime formats, done through saving the dataset as a DataFrame and using a Pandas command
data = squeezed["pcs"].to_dataframe()
data['time'] = data.index
data.reset_index(drop = True, inplace = True)

data['time'] = pd.to_datetime([f"{date.year}-{date.month:02d}-{date.day:02d}" for date in data['time']])

data['Color'] = xr.DataArray(['red' if pcs > bound else 'blue' if pcs < -bound else 'black' for pcs in index["pcs"]])#, dims = index["pcs"].dims, coords = index["pcs"].coords)

rollingAvg = data["pcs"].rolling(window = period, center=True).mean()

fig,ax = plt.subplots(2, 1, figsize=(15,4))

width = (data['time'].iloc[1] - data['time'].iloc[0]).days * 0.9
ax1 = ax[0].bar(data['time'].values, data["pcs"], width = width, color = data['Color'])
ax[0].plot(data['time'], rollingAvg, color='black', linewidth=2, label=f'{period}-Month Rolling Average')

ax2 = ax[1].step(data['time'], neutral)
ax[1].set_ylim(0,2)
ax[1].set_yticks([0,1,2])

plt.show()
