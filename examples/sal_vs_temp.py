import argopy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

f = argopy.DataFetcher()
f
f = f.region([-180, 180, 75, 80, 0, 100, '2010-01', '2014-01'])
f.data

latitude_data = f.data['LATITUDE'].values
longitude_data = f.data['LONGITUDE'].values
pres_data = f.data['PRES'].values #Tried to use d.data here
temp_data = f.data['TEMP'].values
psal_data = f.data['PSAL'].values

df = pd.DataFrame({
    'Latitude': latitude_data,
    'Longitude': longitude_data,
    'depth': pres_data, #pressure represents depth
    'Temperature': temp_data,
    'Salinity': psal_data
})

sns.scatterplot(x='Temperature', y='Salinity', data=df)

plt.title('Scatter Plot of Temperature vs. Salinity')

plt.show()
