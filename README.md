# Open Source Rasters Comparison

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sertit/open_source_rasters_comparison.git/main?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2Fio_and_attributes.ipynb)

Comparisons on different raster features from different Python libraries based on xarray, with or without dask.

This repository contains a series of Jupyter notebooks comparing how open-source Python libraries handle several raster-processing tasks.

The following libraries have been considered :
- rasterio
- rioxarray
- odc-geo
- geoutils


# Notebooks Overview

1. **io_and_attributes.ipynb**
- opening raster files
- reading bands and metadata
- accessing GCPs and RPCs
- saving with different settings : locally, to COG and to Zarr formats
<br>

2. **windows_and_decimation.ipynb**
- reading a dataset by window
- decimating a raster
<br>

3. **reprojection.ipynb**
- reprojecting rasters to a new CRS (without RPC)
- reproject_match a DEM with invalid CRS to a reference raster
<br>

4. **mask_and_crop.ipynb**
- creating spatial masks based on geometry
- cropping rasters to vector polygons or bounding boxes
<br>

5. **merge.ipynb**
- read multiple raster tiles
- combine them into a single raster file
<br>

6. **rasterization_and_vectorization.ipynb**
- rasterizing vector geometries into rasters
- vectorizing raster regions into geometries
<br>

7. **nodata_management.ipynb**
- how nodata values are handled between different libraries 
- pros and cons between NaNs and masked arrays
- nodata interpolation to fill missing values
<br>

8. **usecase_reproj_dask.ipynb**
- usecase on reprojecting a raster and performance comparison with or without dask