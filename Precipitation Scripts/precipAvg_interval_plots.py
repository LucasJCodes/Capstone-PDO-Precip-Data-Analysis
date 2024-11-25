
# Main method to run the functions in precipAvg_interval.py towards average summertime and annual precip in the western US.

import numpy as np
import precipAvg_interval as pcp

filepaths = '/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/PRECTmem*.nc'
data = pcp.pcpAvg(filepaths)

# Make seasons to reference in interval function.
winter = np.arange(0, 3)
spring = np.arange(3, 6)
summer = np.arange(6, 9)
fall = np.arange(9, 12)
seasons = [winter, spring, summer, fall]

# Run interval function to get averages by season.
seasonal_avgs = []
for i in seasons:
    seasonal_avgs.append(pcp.interval(data, i))

#Plot the selected month with prettyColors function.
szn_names = ['Winter', 'Spring', 'Summer', 'Fall']
for i in range(0, 4):
    pcp.prettyColors(seasonal_avgs[i], title = 'Average ' + szn_names[i] + ' Precipitation (mm)', cmap = 'YlGn', save = '/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Plots/' + szn_names[i] + 'AvgPrecip.png')

# Avg Annual Precip
annual = pcp.interval(data, months = np.arange(1, 13))
pcp.prettyColors(annual, title = 'Average Annual Precipitation (mm)', cmap = 'YlGn', save = '/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Plots/AnnualAvgPrecip.png')