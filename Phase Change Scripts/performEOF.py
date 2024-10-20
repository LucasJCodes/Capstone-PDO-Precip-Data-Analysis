def PDO_index(ssts):
    """
    This function computes the Pacific Decadal Oscillation index from a xarray dataset of 
    sea surface temperatures in the North Pacific from 110E to 100W and 20N to 70N and 
    outputs it as an xarray dataset.

    To do this, the function weights SSTs at each grid point by grid area and then uses the 
    eofs package [Dawson 2016] to calculate the  empirical orthogonal function (EOF) 
    of the SST data.  The resulting first principle component is the PDO index.

    :Authors: Lucas Jones in collaboration with Brianna DeFore, Daniel Fenske, Roy Galang


    Dawson A. eofs: A Library for EOF Analysis of Meteorological, Oceanographic, and Climate Data. 
    *Journal of Open Research Software*. 2016;4(1):e14. doi:10.5334/jors.122
    """

    import xarray as xr
    from eofs.xarray import Eof
    from eofs.examples import example_data_path  #for testing purposes
    import numpy as np

    #take the time mean and hold it in a data set 
    #timeAvg = ssts.mean(dim = "time")

    #use the time mean and original data to calulate an anomaly dataset
    #anom = ssts - timeAvg

    file = example_data_path('sst_ndjfm_anom.nc')  #test data
    data = xr.open_dataset(file)['sst']

    #weight the data based on grid cell area by taking the square root of the cosine of latitude
    #store weightings in a numpy array
    #weights = np.sqrt(np.cos(np.deg2rad(anom["lat"].values)))

    #empty_array = np.ones((data["latitude"].size, data['longitude'].size))
    ex_weights = np.sqrt(np.cos(np.deg2rad(data.coords["latitude"].values)))[:, np.newaxis]

    #create and EOF solver object in eofs class
    calc_eof = Eof(data, weights = ex_weights)

    #get the 1st principle component (PC1)
    pc1 = calc_eof.pcs(pcscaling = 1, npcs = 1)

    #output PC1
    return pc1

#testing of the function
from eofs.examples import example_data_path
import matplotlib.pyplot as plt

index = PDO_index(example_data_path('sst_ndjfm_anom.nc'))

fig, axs = plt.subplots()
axs.plot(index[:, 0], color = "black")

fig.savefig("index.png")
