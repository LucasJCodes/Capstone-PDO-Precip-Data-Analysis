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

    #input the data

    #take the time mean and hold it in a data set 

    #use the time mean and original data to calulate an anomaly dataset

    #weight the data based on grid cell area

    #create and EOF solver object in eofs class

    #output principle component 1

