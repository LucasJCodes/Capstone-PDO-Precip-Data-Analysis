# Hi. How are you? Hope you're doing well. Today we are going to make a function that puts all of our fancy EOF and PDO functions together. Enjoy :)

import xarray as xr
import performEOF
import PDOindex

NUM_FILES = 10
phaseChanges = []

#read in all the files using a for loop to add them to the files list
for i in range(11, NUM_FILES + 11):
    #read in the data file for a member
    temp_ds = xr.open_dataset("Data/SSTmem" + str(i) + ".nc", engine = "netcdf4")

    #iterate through the data for the member to calculate the PDO index using the function
    temp_index = performEOF.PDO_index(temp_ds).reset_coords("month", drop = True)

    # Iterate through each of the calculated indices for the different members and find the phase changes
    phaseChanges.append(PDOindex.ID_Phase(temp_index, period = 72, bound = 0.1)[0])
    
#write the list of PDO phase change monthly boolean values in an xarray dataarray 
data_array = xr.DataArray(phaseChanges, dims=["members", "month_bool"], name="is_phase_change")

final = data_array.to_dataset()  #convert the dataarray to a dataset

#write all the data to a file
final.to_netcdf("/Users/lucas/source/repos/Capstone-PDO-Precip-Data-Analysis/Data/phaseChanges.nc")