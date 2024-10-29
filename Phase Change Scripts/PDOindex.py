import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import pandas as pd
import xarray as xr

def ID_Phase(PDOindex, period, bound):
    
    PDOindex['Date'] = pd.to_datetime(PDOindex[['Year', 'Month']].assign(Day=1))

    index = PDOindex["Value"]

    Neutral = False
    NeutralDates = []
    PhaseChange = []

    for i in range(0, len(PDOindex)-period):
        SUM = 0

        for j in range(0, period):
            SUM = SUM + index[i+j]
        
        Average = SUM/period

        if ((Average >= -bound) and (Average <= bound)):
            Neutral = True
            NeutralDates.append(PDOindex['Date'][i])
            PhaseChange.append('1')

        else:
            PhaseChange.append('0')
    
    for i in range(0, period):
        PhaseChange.append('0')
    
    PDOindex['Phase Change'] = PhaseChange

    #print(PDOindex)

    print(len(NeutralDates))

    PDOindex['Color'] = ['red' if value > bound else 'blue' if value < -bound else 'black' for value in PDOindex['Value']]


    fig,ax = plt.subplots(figsize=(15,4))
    ax.bar(PDOindex['Date'], PDOindex['Value'], width=45, color=PDOindex['Color'])
    plt.fill_between(PDOindex['Date'], PDOindex['Value'], 4, where=(PDOindex['Value'] >= -bound), color='lightblue', alpha=0.3, step='mid')
    plt.fill_between(PDOindex['Date'], PDOindex['Value'], 4, where=(PDOindex['Value'] <= bound), color='lightblue', alpha=0.3, step='mid')
    #plt.show()

    plt.figure(figsize=(15,4))
    plt.step(PDOindex['Date'], PDOindex['Phase Change'])
    plt.ylim(0,2)
    plt.show()

    return NeutralDates

############## function end

file = "NOAA_PDO_Index.csv"

NOAAdata = pd.read_csv(file)
PDOindex = pd.DataFrame(NOAAdata)

neutral = ID_Phase(PDOindex, 72, 0.1)
#print(NOAAdata)