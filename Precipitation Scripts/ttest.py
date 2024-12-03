#This method performs a t test on the two given gridded data sets and returns an xarray holding
#gridded pvalues for locations that exceed the significance threshold, alpha.
#The t test is two sidded, performed along the first axis, and assumes equal variance

import numpy as np
from scipy import stats
import xarray as xr
from cartopy.util import add_cyclic_point

def ttest(data1, data2, alpha):
    """
        This function performs a t test on  two given gridded data sets and returns an xarray dataset 
        holding gridded pvalues for locations that exceed the significance threshold, alpha.
        The t test is two sidded, performed along the first axis, and assumes equal variance

        Authors: 
            Lucas Jones in collaboration with Brianna DeFore, Daniel Fenske, Roy Galang

        Args:
            data1- the first xarray dataset to perform the t test on.
            data2- the second xarray dataset to perform the t test on.
            alpha- the significance threshold by which the null hypothesis is tested.

        Returns:
            An array of the p-values which are less than the alpha significance threshold.
        
    """
    print(data1)
    print(data2)
    #perform the t test
    tstat, pval = stats.ttest_ind(data1, data2, axis = 0, equal_var = True, alternative = "two-sided")
    
    #create latitude and longitude arrays for the plotting the p values based on our western US region
    lat = np.arange(25.92, 55, 0.94)  
    lon = np.arange(225, 260, 1.25)  
    
    #print(pval)

    #create a data array holding the p values and add a cyclic point to remove blank line
    xpval = xr.DataArray(pval, coords = {"latitude": lat, "longitude": lon}, dims = ["latitude", "longitude"])

    #get only statistically significant p values for plotting
    
    print(xpval.min())

    sig_pval = xpval.where(xpval.values <= alpha)

    return sig_pval