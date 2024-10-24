import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import pandas as pd

def ID_Phase(data, period, bound):
    
    PDOindex = pd.DataFrame(data)

    PDOindex['Date'] = pd.to_datetime(PDOindex[['Year', 'Month']].assign(Day=1))

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
            NeutralDates.append(PDOindex['Date'][i])


    print(len(NeutralDates))

    PDOindex['Color'] = ['red' if value > bound else 'blue' if value < -bound else 'black' for value in PDOindex['Value']]

    fig,ax = plt.subplots(figsize=(16,4))
    ax.bar(PDOindex['Date'], PDOindex['Value'], width=45, color=PDOindex['Color'])
    plt.show()

    return NeutralDates

############## function end

file = "NOAA_PDO_Index.csv"

NOAAdata = pd.read_csv(file)
neutral = ID_Phase(NOAAdata, 36, 0.5)
#print(NOAAdata)