from requests import get
import json
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
stations = get(url).json()
lons = [station['weather_stn_long'] for station in stations['items']]
lats = [station['weather_stn_lat'] for station in stations['items']]
cc_lat = 0
cc_lon = 0
my_map = Basemap(projection='robin', lat_0 = cc_lat, lon_0 = cc_lon,resolution = 'l')
my_map.drawcoastlines()
my_map.drawcoastlines()
my_map.drawcountries()
my_map.drawstates()
my_map.drawmapboundary()
my_map.drawrivers()
my_map.drawmapboundary(fill_color='aqua')
my_map.fillcontinents(color='green',lake_color='aqua')
x,y = my_map(lons, lats)
my_map.plot(x, y, 'o')
my_map.plot(x, y, 'ro', markersize=12)
cc_lat = 55
cc_lon = 0
my_map = Basemap(projection='merc', lat_0 = cc_lat, lon_0 = cc_lon,resolution = 'h',llcrnrlon=cc_lon-15, llcrnrlat=cc_lat-7,urcrnrlon=cc_lon+5, urcrnrlat=cc_lat+5)
plt.show()
