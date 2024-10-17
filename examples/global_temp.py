import argopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import time
import cartopy.crs as ccrs

# Notes: 
# 1. The script will take longer to run the first rime it is run (~ 5 min)
# 2. If you get a timeout error, try running on a different machine or a better network
# 3. After the first time running, .csv files will be stored locally for faster recall
# 4. Timeout limitations are due to Argo servers, not python file.

# define parameters :

dates_list = [['2015-01', '2015-02'], ['2015-04', '2015-05'], ['2015-07', '2015-08'], ['2015-10', '2015-11']]
argopy.set_options(src='erddap', dataset='phy', mode='standard')


def plot_data() :
    for i, dates in enumerate(dates_list) :

        file = 'data'+str(i+1)+'.csv'

        print("Starting task " + str(i+1))

        try :
            df = pd.read_csv(file)
        except :
            print("Importing data...")
            t0 = time.time()
            ArgoSet = argopy.DataFetcher().region([-180,180,-90,90, 0, 5] + dates)
            split = time.time()-t0
            print("Time to import : ", split)
            t0 = time.time()
            ds = ArgoSet.data.argo.point2profile()
            split = time.time()-t0
            print("Time to get data from DataFetcher : ", split)
            t0 = time.time()
            df = ds.to_dataframe()
            split = time.time()-t0
            print("Time to convert : ", split)
            df.to_csv(file) 

        # Define the variables to work with:
        temp = np.array(df['TEMP'])
        lat = np.array(df['LATITUDE'])
        long = np.array(df['LONGITUDE'])

        print("Plotting data...")

        fig = plt.figure()
        ax = plt.axes(projection=ccrs.PlateCarree())
        ax.coastlines()
        global_temp = ax.scatter(long, lat, c=temp)

        # title and label :
        cbar = fig.colorbar(global_temp, location='bottom')
        cbar.set_label('Celsius')
        ax.set_title('Sea Surface Temperature' + ' ' + dates[0] + ' to ' + dates[1])
        gridlines = ax.gridlines(draw_labels=True) # shows lat/long
        
        plt.savefig('figures/global_temp' + str(i+1) + '.png')
    
    return True
        # plt.show()



if __name__ == "__main__" :
   
   flag = False
   while not flag :
        try : flag = plot_data()
        except :
            print("Argo Server Timeout Error : retrying")
            print("To exit, press ctrl+c 2x")
            time.sleep(2)
            
   