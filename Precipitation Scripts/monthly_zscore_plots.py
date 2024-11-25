'''
This code will plot the average z-scores for a specific month
We need the monthly plots of z-scores during phase changes

Good codes to look at: 
    zscores_average (precip z-scores for phase change months)
    precip_zscores (has a plot looking at a particular month, though will need to change based on what the original meant to plot)
'''

import xarray as xr
import zscores_average
import precip_zscores
import glob
import precipAvg_interval as pcp

#Some of this code is a copy-paste from previous Python files (see above - this one is for zscores_average). Since we want all members, that part will be kept.

# Retrieve the precip files, sorted so that each member is in order.
filenames = sorted(glob.glob('/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/PRECTmem*.nc'))

# Calculate the z-scores for each member, then concatenate them with a new "members" dimension.
zscores = [precip_zscores.member_zscore(f) for f in filenames]
zscores = xr.concat(zscores, dim = 'members')

# Read in the booleans that define which months are phase changes.
bools = xr.open_dataset('/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/phaseChanges.nc')
# Rename the month_bool dimension to "time" so that it can be multiplied directly into zscores inside the function.
bools = bools.rename({"month_bool": "time"})

# Run the function.
test = zscores_average.phaseMask(zscores, bools)

# Group times by month, then take the mean across members and months. Taking the mean ignores NaNs from the function.
grouped = test.groupby('time.month')
grouped = grouped.mean(dim = ['members', 'time'])

# Print the result!
print(grouped)

#PLOTTING CONTOUR MAPS (this part is somewhat new?)

# Might need these line, but let's see first
# data['time'] = data['time'].dt.strftime('%Y%m%d')

#Dictionary for the months
months = {'1': 'January', '2': 'February', '3': 'March',
          '4': 'April', '5': 'May', 
          '6': 'June', '7': 'July', '8': 'August', 
          '9': 'September', '10': 'October', '11': 'November', '12': 'December',}

# For loop that will go through each month and create a plot of the average precip zscores of all members
for month in grouped['month']:
    # Choose which month to plot
    selected_by_month = grouped.where((grouped.month == month), drop = True)
    selected_by_month = selected_by_month.squeeze(('month'), drop = True)

    #Find the correct month for the title
    month_dict_value = month.item() #converts into integer
    month_dict_value = str(month_dict_value) #converts into string
    month_name = months.get(month_dict_value)
    
    #Plot the selected month
    title = "Zscore for all members in the month of " + str(month_name)
    pcp.prettyColors(selected_by_month, title, cmap = 'BrBG', save = "/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Plots/"+month_name+'_zscore.png', vmin = -0.36, vmax = 0.36)

    