import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import json
import matplotlib.patheffects as PathEffects


plt.figure(figsize=(10,8))

ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()#giving us continent boundaries
ax.stock_img()#giving us the colors (white means icy continents or countries)

arr = [
    
    # {   "latitude" : 21.4266667, "longitude" : 39.8261111, "city" : "Mecca" }, 
    # {   "latitude" : 24.8666667, "longitude" :  67.05, "city" : "Karachi" }, 
    # {   "latitude" : 31.55800000, "longitude" : 74.35071000, "city" : "Lahore" }, 
    # {   "latitude" : 33.684389, "longitude" : 73.047505, "city" : "Islamabad" }, 
    # {   "latitude" : 34.0083333, "longitude" : 71.5727778, "city" : "Peshawar" }, 
    # {   "latitude" : 25.2638889, "longitude" : 63.4744444, "city" : "Pasni" }, 
    # {   "latitude" : 30.179778, "longitude" : 66.974911, "city" : "Quetta" }, 
    # {   "latitude" : 36.2666667, "longitude" : 74.6833333, "city" : "Hunza" },
    {   "latitude" : 29.8002778, "longitude" : 72.1758333, "city" : "Mailsi" }, 
    {   "latitude" : 24.524621, "longitude" : 39.569273, "city" : "Medina" }, 
    {   "latitude" : 34.052239, "longitude" : -118.243398, "city" : "LA" }, 
    {   "latitude" : 40.730610, "longitude" : -73.935242, "city" : "NYC"  }, 
    {   "latitude" : 33.628342, "longitude" : -117.927933, "city" : "Newport Beach"  }, 
    {   "latitude" : 41.015137, "longitude" : 28.979530, "city" : "Istanbul" }, 
    {   "latitude" : 37.532600, "longitude" : 127.024612, "city" : "Seoul" }, 
    {   "latitude" : 48.864716, "longitude" : 2.349014, "city" : "Paris" }, 

] 

arrayLogLat = json.dumps(arr)
data = json.loads(arrayLogLat)

#Location 
for i in data: 
    plt.scatter(i["longitude"], i["latitude"], marker='P', color='red', s=100, edgecolor='black' )#show lahore on map
    txt=plt.text(i["longitude"], i["latitude"], s=i["city"], color = 'black', fontdict={'weight': 'book', 'size': 10, 'ha': 'left', 'va': 'bottom', 'family': 'cursive'})
    txt.set_path_effects([PathEffects.withStroke(linewidth=2, foreground='w')])# add outline to text
    plt.draw()

plt.title('Cities I Need to Visit One Day', fontsize=16, weight='bold') 

plt.show()
