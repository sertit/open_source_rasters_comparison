# Open Source Rasters Comparison

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sertit/open_source_rasters_comparison.git/main?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2F01_io_and_attributes.ipynb)

Comparisons on different raster features from different Python libraries based on `xarray`, with or without `dask`.

This repository contains a series of Jupyter notebooks comparing how open-source Python libraries handle several raster-processing tasks.

The following libraries have been considered :
- `rasterio`
- `rioxarray`
- `odc-geo`
- `geoutils`
- `xarray-spatial`
<br><br>


# Notebooks Overview

### 📖 [**01_io_and_attributes.ipynb**](notebooks/01_io_and_attributes.ipynb)
- opening raster files
- reading bands and metadata
- accessing GCPs and RPCs
- saving with different settings : locally, to COG and to Zarr formats
<br>

### 🪟 [**02_windows_and_decimation.ipynb**](notebooks/02_windows_and_decimation.ipynb)
- reading a dataset by window
- decimating a raster
<br>

### 📽️ [**03_reprojection.ipynb**](notebooks/03_reprojection.ipynb)
- reprojecting rasters to a new CRS (without RPC)
- reproject_match a DEM with invalid CRS to a reference raster
<br>

### 🎭 [**04_mask_and_crop.ipynb**](notebooks/04_mask_and_crop.ipynb)
- creating spatial masks based on geometry
- cropping rasters to vector polygons or bounding boxes
<br>

### 🔗 [**05_merge.ipynb**](notebooks/05_merge.ipynb)
- read multiple raster tiles
- combine them into a single raster file
<br>

### 🗺️ [**06_rasterization_and_vectorization.ipynb**](notebooks/06_rasterization_and_vectorization.ipynb)
- rasterizing vector geometries into rasters
- vectorizing raster regions into geometries
<br>

### 🗄️ [**07_nodata_management.ipynb**](notebooks/07_nodata_management.ipynb)
- how nodata values are handled between different libraries 
- pros and cons between NaNs and masked arrays
- nodata interpolation to fill missing values
<br>

### 🎯 [**08_usecase_reproj_dask.ipynb**](notebooks/08_usecase_reproj_dask.ipynb)
- usecase on reprojecting a raster and performance comparison with or without dask