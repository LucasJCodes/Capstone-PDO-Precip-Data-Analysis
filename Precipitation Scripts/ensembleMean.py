import xarray as xr

def ensMean(data):
    """
    This function computes the mean of precipitation data from a multi-member ensemble of the CESM2-LE experiment.

    Authors: 
        Lucas Jones in collaboration with Brianna DeFore, Daniel Fenske, Roy Galang

    Args:
        data- the xarray datasets to perform the calculation on.
        

    Returns:
        An xarray dataset that holds the ensemble mean of precipitation data for 10 members
        
    """

    #calculate the mean along the members and by time
    byTime = data.groupby("time.month")
    ensAvg = data.mean(dim = ["members", "time"])

    #return the dataset 
    return ensAvg

##############

"""
filenames = "Data/PRECTmem*.nc"

avgs = ensMean(filenames)

test = xr.open_dataset("Data/PRECTmem11.nc")
print(test)
"""
