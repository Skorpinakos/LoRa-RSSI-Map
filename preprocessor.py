import os
import json
import matplotlib.pyplot as plt
import numpy as np
class Event:
    def __init__(self,file_path):
        #print(file_path)
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            self.time=data["time"]
            self.lat=data["object"]["location"]["latitude"]
            self.lon=data["object"]["location"]["longitude"]
            self.gateways=[]
            self.rssis=[]
            for gateway in data["rxInfo"]:
                try:
                    self.gateways.append([gateway["gatewayId"],gateway["rssi"],gateway["snr"]])
                except:
                    self.gateways.append([gateway["gatewayId"],gateway["rssi"]])
                self.rssis.append(gateway["rssi"])
                self.max_rssi=max(self.rssis)


def get_json_files(directory):
    json_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            json_files.append(directory+filename)
    return json_files
def filter_dragino(json_list):
    filtered=[]
    trash=[]
    for file in json_list:
        if is_word_present_in_json(file,"Dragino"):
            filtered.append(file)
        else:
            trash.append(file)
    print("packets:",len(filtered))
    return filtered

def is_word_present_in_json(file_path, word):
    with open(file_path, 'r') as json_file:
        data = str(json_file.read())
    if word in data:
        return True
    else:
        return False


directory_path = "pos_server2/" 
json_files_list = get_json_files(directory_path)
filtered_list=filter_dragino(json_files_list)
points=[]
for entry in filtered_list:
    with open(entry, 'r') as json_file:
        data = json.load(json_file)
        if str(data["object"]["location"]["latitude"])!='-677.7216':
            points.append(Event(entry))
            print(len(points))
#print(points[0].max_rssi)
points.sort(key=lambda x : x.time )
#points=points[0:170]
with open('log.csv','w',encoding='utf-8') as file:
    file.write("")
with open('log.csv','a',encoding='utf-8') as file:
    for point in points:
        file.write(str(point.lat)+","+str(point.lon)+","+str(point.max_rssi/-1)+'\n')

# Setup
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
params = {'font.size'     : 14,
          'figure.figsize':(15.0, 8.0),
          'lines.linewidth': 2.,
          'lines.markersize': 15,}
matplotlib.rcParams.update(params)

Ni = len(points)
Xi= np.array([x.lon for x in points])
Xi=Xi-(sum(Xi)/len(Xi))
Xi=Xi*100000
Yi= np.array([x.lat for x in points])
Yi=Yi-(sum(Yi)/len(Yi))
Yi=Yi*100000
Zi= np.array([x.max_rssi for x in points])
print(Xi)


import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()


from scipy.spatial import Delaunay
Pi = np.array([Xi, Yi]).transpose()
tri = Delaunay(Pi)


N = 4000
x = np.linspace(-2000., 2000., N)
y = np.linspace(-2000., 2000., N)
X, Y = np.meshgrid(x, y)
P = np.array([X.flatten(), Y.flatten() ]).transpose()
#plt.plot(Xi, Yi, "or", label = "Data")
#plt.triplot(Xi, Yi , tri.simplices.copy())
#plt.plot(X.flatten(), Y.flatten(), "g,", label = "Z = ?")
#plt.legend()
#plt.grid()
#plt.show()

from scipy.interpolate import griddata
Z_cubic = griddata(Pi, Zi, P, method = "linear").reshape([N, N])
plt.contourf(X, Y, Z_cubic, 100, cmap = mpl.cm.jet)
plt.colorbar()
#plt.contour(X, Y, Z_cubic, 20, colors = "k")
#plt.triplot(Xi, Yi , tri.simplices.copy(), color = "k")
plt.scatter(Xi, Yi, s=1)
plt.legend()
plt.grid()
plt.show()