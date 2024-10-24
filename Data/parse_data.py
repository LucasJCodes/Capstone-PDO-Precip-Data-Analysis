import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
'''
This file holds a method to combined and then subset by latitude and longitude a given set of data 
meteorological data sets that are spread over multiple files.  For example, if a single data set
is divided into groups by years this can read in each separate file for the year/period of the same
data, combine it, and then subset it over the given latitude and longitude bounds.

Authors: 
        Lucas Jones in collaboration with Brianna DeFore, Daniel Fenske, Roy Galang

Args:
        filenames: an string holding the path and name(s) of a file(s) holding the raw data.
        s_bound: The southern bound to subset the data over in degrees latitude.
        n_bound: The northern bound to subset the data over in degrees latitude.
        e_bound: The eastern bound to subset the data over in degrees latitude.
        w_bound: The western bound to subset the data over in degrees latitude.

Returns:
        data: An xarray data set holding the combined and subsetted data.
'''
def latlon_subset(filenames, s_bound, n_bound, e_bound, w_bound):

    data_in = xr.open_mfdataset(filenames)

    lat_parse = data_in.sel(lat = slice(s_bound, n_bound))

    data = lat_parse.sel(lon = slice(e_bound, w_bound))

    return data

########## End of Function, main method calling function for SST data ########################

#path in your file system to the data
path = "\\Users\\17135\\Capstone Code\\Capstone-PDO-Precip-Data-Analysis\\"

#iterate through each ensemble member set of files
for i in range(11, 21):

    #generate the file names corresponding to a given member across all years
    files = path + "b.e21.B*smbb.f09_g17.LE2-1301.0" + str(i) + ".cam.h0.SST.*.nc"

    print("here" + files)

    data = latlon_subset(files, 20, 70, 110, 260)

    #save the subsetted data to the local folder as a file with the member name in it.
    data["SST"].to_netcdf("SSTmem" + str(i) + ".nc")