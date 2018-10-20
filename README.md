# Schlauchautomat-Finder
On https://www.continental-reifen.de/fahrrad/schlauch-automat, Continental provides a map with all their tube vending machines in Germany.

The following API endpoint allows to extract all vending machines for a given bounding box: https://contiserver.de/extern/search/public_api/search/json/m/70/latmin/xx.xx/lngmin/xx.xx/latmax/xx.xx/lngmax/xx.xx
In this example, the bounding box for entire Germany (5.98865807458, 47.3024876979, 15.0169958839, 54.983104153) has been used which leads to the URL https://contiserver.de/extern/search/public_api/search/json/m/70/latmin/47.3024876979/lngmin/5.98865807458/latmax/54.983104153/lngmax/15.0169958839

*WATCH OUT*: The URL structure is different to the usual `bbox = min Longitude , min Latitude , max Longitude , max Latitude` bounding box structure and needs to be modified when filling in the values!

The script converts the JSON served by the Continental API into a .csv file that can for example be uploaded into a Google Maps. See as an example: https://drive.google.com/open?id=1JU-_Sd7s8g0JkgAHraLpNi9O_g6iy0l3&usp=sharing
