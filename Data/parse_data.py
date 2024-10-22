import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def latlon_subset(filenames, s_bound, n_bound, e_bound, w_bound):

    data_in = xr.open_mfdataset(filenames)

    lat_parse = data_in.sel(nlat = slice(s_bound, n_bound))

    data = lat_parse.sel(nlon = slice(e_bound, w_bound))

    return data

path = "your/path/to/raw/data"

for i in range(11, 21):

    files = path + "b.e21.B*smbb.f09_g17.LE2-1301.0" + str(i) + ".cam.h0.SST.*.nc"

    print(files) 

    data = latlon_subset(files, 20, 70, 110, 260)

    data["SST"].to_netcdf("SSTmem" + str(i) + ".nc")