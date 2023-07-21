import os
import json
import gmaps
from IPython.display import display
gmaps.configure(api_key='AIzaSyAwDWelap9K-oCk3prpQDru1igAu9GRUJQ')
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

if __name__ == "__main__":
    directory_path = "pos_server/" 
    json_files_list = get_json_files(directory_path)
    filtered_list=filter_dragino(json_files_list)
    points=[]
    for entry in filtered_list:
        points.append(Event(entry))
    print(points[0].max_rssi)

    locations = [(51.5, 0.1), (51.7, 0.2), (51.4, -0.2), (51.49, 0.1)]

    heatmap_layer = gmaps.heatmap_layer(locations)
    fig = gmaps.figure()
    fig.add_layer(heatmap_layer)
    display(fig)