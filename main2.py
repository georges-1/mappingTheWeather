from requests import get
import json
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getalllastmeasurement'
station_data = get(url).json()
lons = [data['weather_stn_long'] for data in station_data['items']]
lats = [data['weather_stn_lat'] for data in station_data['items']]
temps = [data['ambient_temp'] for data in station_data['items']]
cc_lat = int(input("What is the latitude: "))
cc_lon = int(input("What is the longatude: "))
my_map = Basemap(projection='merc', lat_0 = cc_lat, lon_0 = cc_lon,
resolution = 'h' , area_thresh = 1,
llcrnrlon=cc_lon-15, llcrnrlat=cc_lat-7,
urcrnrlon=cc_lon+5, urcrnrlat=cc_lat+5)
my_map.drawcoastlines()
my_map.drawcountries()
my_map.drawmapboundary()
my_map.bluemarble()
for lon, lat, temp in zip(lons, lats, temps):
    if lon >= cc_lon-15 and lon <= cc_lon+5 and lat >= cc_lat-7 and lat <= cc_lat+5:
        x,y = my_map(lon, lat)
        my_map.plot(x, y, 'o', markersize=10, color=(0,0,1))
        plt.text(x, y, temp, color = 'w', ha='right',va='bottom')
plt.show()
