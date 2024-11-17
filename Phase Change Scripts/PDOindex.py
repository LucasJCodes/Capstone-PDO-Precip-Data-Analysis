import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import pandas as pd
import xarray as xr

def ID_Phase(PDOindex, period, bound):
    
    PDOindex['Phase Change'] = 0

    """
    NeutralDates = np.full((len(PDOindex) - period, 1), np.NaN)
    NeutralDates = NeutralDates.astype(datetime)
    """

    NeutralDates = []
    phaseBool = []

    for i in range(0, len(PDOindex)-period):
        SUM = 0

        for j in range(0, period):
            SUM = SUM + PDOindex[i+j]
        
        Average = SUM/period

        if ((Average >= -bound) and (Average <= bound)):
            CentralMonth = i + period // 2
            NeutralDates.append((PDOindex.time[CentralMonth].values).item())
            phaseBool.append(1)

        else:
            phaseBool.append(0)

    print(len(NeutralDates))

    return phaseBool, NeutralDates

############## function end
"""
file = "NOAA_PDO_Index.csv"
bound = 0.1
mon_length = 72

NOAAdata = pd.read_csv(file)
PDOindex = pd.DataFrame(NOAAdata)

neutral = ID_Phase(PDOindex, mon_length, bound)
#print(NOAAdata)

PDOindex['Color'] = ['red' if value > bound else 'blue' if value < -bound else 'black' for value in PDOindex['Value']]

fig,ax = plt.subplots(figsize=(15,4))
ax.bar(PDOindex['Date'], PDOindex['Value'], width=45, color=PDOindex['Color'])
plt.fill_between(PDOindex['Date'], PDOindex['Value'], 4, where=(PDOindex['Value'] >= -bound), color='lightblue', alpha=0.3, step='mid')
plt.fill_between(PDOindex['Date'], PDOindex['Value'], 4, where=(PDOindex['Value'] <= bound), color='lightblue', alpha=0.3, step='mid')

fig2,ax2 = plt.subplots(figsize=(15,4))
ax2.step(PDOindex['Date'], PDOindex['Phase Change'])
ax2.set_ylim(0,2)
ax2.set_yticks([0,1,2])

plt.show()
"""