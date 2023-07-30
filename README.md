This is a LoRa antenna RSSI heatmaping project.

Continuing work from [this repo](https://github.com/thanospan/dragino-lora-gps)

Use the hats on the arduino to provide GPS and LoRa interfaces

![239218546-3891f6f5-7461-4838-89cc-31637bc0f311](https://github.com/Skorpinakos/lora_map_v2/assets/82767099/24e2389f-488d-403a-90c3-de3ef8e93085)

Gather the points through a chirpstack intergration and a python http server.

Then collect each 3D point (lat,lon,RSSI) :
![2D_Interpolation_4_0](https://github.com/Skorpinakos/lora_map_v2/assets/82767099/f6b24d63-f4f2-4b39-87f9-d9fa5448bf06)

Extrude a non overlapping 2D graph :
![2D_Interpolation_6_0](https://github.com/Skorpinakos/lora_map_v2/assets/82767099/c24fdd0b-50c4-4e3a-913c-46ce9c0ab49f)

Use 2D linear interpolation to fill empty space :
![2D_Interpolation_15_0](https://github.com/Skorpinakos/lora_map_v2/assets/82767099/9c63d0a8-82e1-4b0a-ac70-b84e613e074d)

Then overlap semi transparent heatmap (with 500+ points) on the actual map :
![V2](https://github.com/Skorpinakos/lora_map_v2/assets/82767099/ec0517be-cf87-47ef-9aa7-f3de5f2689b0)

Early version with just ~160 points :
![end_result_with_bar](https://github.com/Skorpinakos/lora_map_v2/assets/82767099/adecd9e7-ad76-4bdb-b53c-13c9317ae2a6)






