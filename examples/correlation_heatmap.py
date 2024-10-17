import argopy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

f = argopy.DataFetcher()
f
f = f.region([-180, 180, -90, 90, 0, 20, '2011-01', '2013-01'])
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

print(df)
Var_Corr = df.corr()

# Set up the annotation parameters (font size, weight, and other properties)
annot_kws = {"size": 12, "weight": "bold"}

# Set up the color bar parameters (font size, weight, and other properties)
cbar_kws = {"shrink": 0.75, "ticks": np.arange(-1, 1.1, 0.2)}

# Plot the heatmap with correlation values in the center
plt.figure(figsize=(12, 10))
heatmap = sns.heatmap(Var_Corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5, center=0, annot_kws=annot_kws, cbar_kws=cbar_kws)

# Set the x-axis and y-axis tick labels to bold
heatmap.set_xticklabels(heatmap.get_xticklabels(), weight="bold", size=12)
heatmap.set_yticklabels(heatmap.get_yticklabels(), weight="bold", size=12)

plt.title('Correlation Heatmap')
plt.show()
