# This is a LoRa antenna RSSI heatmaping project.

## Continuing work from [this repo](https://github.com/thanospan/dragino-lora-gps)

### Use the hats on the arduino to provide GPS and LoRa interfaces

![239218546-3891f6f5-7461-4838-89cc-31637bc0f311](https://github.com/Skorpinakos/LoRa-RSSI-Map/assets/82767099/eaf94300-68c9-4002-924e-85e434409dc3)


### Gather the points through a chirpstack intergration and a python http server.

### Then collect each 3D point (lat,lon,RSSI) :
![2D_Interpolation_4_0](https://github.com/Skorpinakos/LoRa-RSSI-Map/assets/82767099/0d0a2d03-4a35-47c2-bf5f-9d6e9da2f812)



### Extrude a non overlapping 2D graph :
![2D_Interpolation_4_0](https://github.com/Skorpinakos/LoRa-RSSI-Map/assets/82767099/9836c76e-e197-4d12-bcec-10ce9f8a533c)



### Use 2D linear interpolation to fill empty space :
![2D_Interpolation_15_0](https://github.com/Skorpinakos/LoRa-RSSI-Map/assets/82767099/c8bcac6b-1b59-43c7-a29d-520be3d3aee2)


## Then overlap semi transparent heatmap (with 500+ points) on the actual map :
![V2](https://github.com/Skorpinakos/LoRa-RSSI-Map/assets/82767099/a2c9f650-d7e4-454e-8688-671c3ec06e20)



### Early version with just ~160 points :
![end_result_with_bar](https://github.com/Skorpinakos/LoRa-RSSI-Map/assets/82767099/a2155bd1-b144-4f35-b484-8ec6b7bfd306)







