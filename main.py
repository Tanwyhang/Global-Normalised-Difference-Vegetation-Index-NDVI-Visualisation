import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import os

skip = 1

dir = os.getcwd()


# world = "worldmap_raster.tif"
world = dir + r"\worldmap_raster.tif"


with rasterio.open(world) as source:
    world = source.read()
    world_data_first_band = source.read(1)
    world_data_second_band = source.read(2)

world_data_first_band = world_data_first_band.astype(float) # Red band
world_data_second_band = world_data_second_band.astype(float) # NIR band

# add offset
nvdi = (world_data_second_band - world_data_first_band) / (world_data_first_band + world_data_second_band + 1*10**(-10))


plt.figure(clear=True)
plt.axis('off')
# ndvi color scheme RdYlGn
show(nvdi, cmap="magma")
plt.show()
