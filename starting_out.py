import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt

# Open the NVDI raster image
nvdifile = r"C:\Users\60164\Desktop\Programming 2024\Geographic Information System (GIS)\HYP_LR_SR_W.tif"
with rasterio.open(nvdifile) as src:
    nvdidata = src.read()  # Read the first band (assuming NVDI is stored in the first band)

# Plot NVDI image
plt.figure()
show(nvdidata, cmap='plasma')  # Using RdYlGn colormap for NVDI
plt.colorbar(label='NVDI Value')
plt.title('Normalized Difference Vegetation Index (NVDI)')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.show()
