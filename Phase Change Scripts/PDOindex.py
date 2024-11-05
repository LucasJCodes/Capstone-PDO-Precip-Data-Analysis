import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import pandas as pd
import xarray as xr

def ID_Phase(PDOindex, period, bound):
    
    PDOindex['Date'] = pd.to_datetime(PDOindex[['Year', 'Month']].assign(Day=1))
    PDOindex['Phase Change'] = 0

    index = PDOindex["Value"]

    Neutral = False
    NeutralDates = []


    for i in range(0, len(PDOindex)-period):
        SUM = 0

        for j in range(0, period):
            SUM = SUM + index[i+j]
        
        Average = SUM/period

        if ((Average >= -bound) and (Average <= bound)):
            Neutral = True
            CentralMonth = i + period // 2
            NeutralDates.append(PDOindex['Date'][CentralMonth])
            PDOindex.at[CentralMonth, 'Phase Change'] = 1

    #print(PDOindex)

    print(len(NeutralDates))

    PDOindex['Color'] = ['red' if value > bound else 'blue' if value < -bound else 'black' for value in PDOindex['Value']]


    fig,ax = plt.subplots(figsize=(15,4))
    ax.bar(PDOindex['Date'], PDOindex['Value'], width=45, color=PDOindex['Color'])
    plt.fill_between(PDOindex['Date'], PDOindex['Value'], 4, where=(PDOindex['Value'] >= -bound), color='lightblue', alpha=0.3, step='mid')
    plt.fill_between(PDOindex['Date'], PDOindex['Value'], 4, where=(PDOindex['Value'] <= bound), color='lightblue', alpha=0.3, step='mid')
    #plt.show()

    fig2,ax2 = plt.subplots(figsize=(15,4))
    ax2.step(PDOindex['Date'], PDOindex['Phase Change'])
    ax2.set_ylim(0,2)
    ax2.set_yticks([0,1,2])

    plt.show()

    return NeutralDates

############## function end

file = "NOAA_PDO_Index.csv"

NOAAdata = pd.read_csv(file)
PDOindex = pd.DataFrame(NOAAdata)

neutral = ID_Phase(PDOindex, 72, 0.1)
#print(NOAAdata)