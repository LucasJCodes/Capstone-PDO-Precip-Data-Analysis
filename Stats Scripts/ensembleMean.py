def ensMean(files):
    """
    This function computes the mean 

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

    #open each member's precip into an xarray data set
    data = xr.open_mfdataset(files, combine = 'nested', concat_dim = 'member')

    #calculate the mean along the members and by time
    byTime = data.groupby("time.month")
    ensAvg = data.mean(dim = ["member", "time"])

    #return the dataset 
    return ensAvg

##############

"""
filenames = "Data/PRECTmem*.nc"

avgs = ensMean(filenames)
"""
