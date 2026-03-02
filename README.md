# fivem-vehicle-packer
CLI tool made in python to quickly pack a large amount of FiveM vehicle resources into a single resource.


## How to use
1. Place all your existing vehicle resources into a new folder
2. Ensure all the vehicle resources follow this format (If you have more stream or data files the script will automatically find them):
```filetree
vehicleresource/
├── stream/
│   ├── vehicle.yft
│   ├── vehicle_hi.yft
│   └── vehicle.ytd
├── handling.meta
├── vehicles.meta
├── carvariations.meta
├── vehiclelayouts.meta
└── __resource.lua or fxmanifest.lua
```
3. Run the script (Python 3.12.10 was used to create it)
4. Paste or type the path to folder where all the vehicle resources are (Example: C:\Users\for0one\FiveM\vehicleResources)
5. Give a name for the vehicle pack folder
6. Give a description for the pack manifest
7. Wait for the pack to be create in the path you set in Step 4, the path will also be printed to the console
8. Check a few folders to ensure everything looks normal
9. Add it to your FiveM server and restart! (I'd recommed to clear your servers cashe after adding a pack if you already had those vehicles in the server)
