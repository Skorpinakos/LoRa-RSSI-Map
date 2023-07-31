# This is a LoRa antenna RSSI heatmaping project.

## Continuing work from [this repo](https://github.com/thanospan/dragino-lora-gps)

### Use the hats on the arduino to provide GPS and LoRa interfaces

![239218546-3891f6f5-7461-4838-89cc-31637bc0f311](https://github.com/Skorpinakos/LoRa-RSSI-Map/assets/82767099/eaf94300-68c9-4002-924e-85e434409dc3)


### Gather the points through a chirpstack intergration and a python http server.
![download (5)](https://github.com/Skorpinakos/LoRa-RSSI-Map/assets/82767099/92324101-0ffd-4bc2-bb7c-83c0be2b68d2)


### Then collect each 3D point (lat,lon,RSSI) :
![2D_Interpolation_4_0](https://github.com/Skorpinakos/LoRa-RSSI-Map/assets/82767099/0d0a2d03-4a35-47c2-bf5f-9d6e9da2f812)



### Extrude a non overlapping 2D graph :
![2D_Interpolation_6_0](https://github.com/Skorpinakos/LoRa-RSSI-Map/assets/82767099/7f51564e-b134-4911-b29f-80875a1ee37e)




### Use 2D polynomial interpolation to fill empty space :
![2D_Interpolation_15_0](https://github.com/Skorpinakos/LoRa-RSSI-Map/assets/82767099/c8bcac6b-1b59-43c7-a29d-520be3d3aee2)

### Early version with just ~160 points :
![end_result_with_bar](https://github.com/Skorpinakos/LoRa-RSSI-Map/assets/82767099/a2155bd1-b144-4f35-b484-8ec6b7bfd306)







