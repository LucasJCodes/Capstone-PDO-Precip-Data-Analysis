
# Main method to run the functions in precipAvg_interval.py towards average summertime and annual precip in the western US.

import numpy as np
import precipAvg_interval as pcp

filepaths = '/Users/dfencekey/Desktop/Coding/Capstone/Capstone-PDO-Precip-Data-Analysis/Data/PRECTmem*.nc'
data = pcp.pcpAvg(filepaths)

# Avg Summertime Precip
summertime = pcp.interval(data, months = np.arange(6, 9))
pcp.prettyColors(data = roy, title = 'Average Summertime Precipitation (mm)', cmap = 'YlGn', save = 'avgSummer_precip.png')

# Avg Annual Precip
annual = pcp.interval(data, months = np.arange(1, 13))
pcp.prettyColors(data = daniel, title = 'Average Annual Precipitation (mm)', cmap = 'YlGn', save = 'avgAnnual_precip.png')