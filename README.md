# Open Source Rasters Comparison

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sertit/open_source_rasters_comparison.git/main?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2F01_io_and_attributes.ipynb)

## Context & Goal

This repository presents a benchmark and hands-on comparison of open-source Python libraries for geospatial raster processing.

Its objective is twofold:
- **Compare** how different Python ecosystems handle common Earth observation and GIS raster operations (I/O, reprojection, masking, merging, vectorization, nodata handling, and Dask-based scaling).
- **Provide a practical entry point** for developers and geospatial practitioners (from beginners to advanced users) looking to choose the right library for their workflow.

---

## Libraries Compared

| Library | Core Data Model | `xarray` Integration | `dask` (Lazy / Chunked) |
| :--- | :--- | :--- | :--- |
| **`rasterio`** | NumPy arrays + GDAL dataset handles | Manual | Via `rioxarray` or custom windowing |
| **`rioxarray`** | `xarray.DataArray` / `Dataset` | Native (`rio` accessor) | Native |
| **`odc-geo`** | `xarray` + `GeoBox` | Native (`odc` accessor) | Native |
| **`geoutils`** | Custom `Raster` object (NumPy / MaskedArray) | Experimental / accessor | Partial |
| **`xarray-spatial`** | `xarray.DataArray` | Native | Native (Numba / Dask) |

---

## Getting Started

### 1. Set up the environment

You can create the Conda environment (Python 3.13) from [`environment.yml`](environment.yml):

```bash
conda env create -f environment.yml
conda activate open_source_rasters_comparison
```

Alternatively, install the dependencies in an existing Python environment using [`requirements.txt`](requirements.txt):

```bash
pip install -r requirements.txt
```

### 2. Download the sample data

The notebooks rely on sample raster and vector datasets stored in `data/`. Download and extract them automatically by running [`scripts/download_data.py`](scripts/download_data.py) from the repository root:

```bash
python scripts/download_data.py
```

This script downloads the archive and extracts it into `data/rasters` and `data/vectors`.

---

## Notebooks Overview

| Notebook | Topic | What you will learn |
| :--- | :--- | :--- |
| 📖 [**01_io_and_attributes.ipynb**](notebooks/01_io_and_attributes.ipynb) | **Input / Output & Attributes** | Opening rasters, inspecting bands and metadata, accessing GCPs/RPCs, and saving locally or to COG / Zarr formats. |
| 🪟 [**02_windows_and_decimation.ipynb**](notebooks/02_windows_and_decimation.ipynb) | **Windows & Decimation** | Reading subsets of large rasters by spatial/pixel windows and downsampling (decimation) for previews or fast processing. |
| 📽️ [**03_reprojection.ipynb**](notebooks/03_reprojection.ipynb) | **Reprojection** | Reprojecting rasters to a target CRS and aligning (`reproject_match`) a DEM with an invalid CRS to a reference raster. |
| 🎭 [**04_mask_and_crop.ipynb**](notebooks/04_mask_and_crop.ipynb) | **Mask & Crop** | Creating spatial masks from vector geometries and cropping rasters to polygons or bounding boxes. |
| 🔗 [**05_merge.ipynb**](notebooks/05_merge.ipynb) | **Merge** | Reading multiple raster tiles and mosaicking them into a single continuous raster. |
| 🗺️ [**06_rasterization_and_vectorization.ipynb**](notebooks/06_rasterization_and_vectorization.ipynb) | **Rasterization & Vectorization** | Converting vector geometries into raster grids and extracting vector polygons from raster regions. |
| 🗄️ [**07_nodata_management.ipynb**](notebooks/07_nodata_management.ipynb) | **Nodata Management** | Understanding how each library handles nodata (`NaN` vs masked arrays) and interpolating missing values. |
| 🎯 [**08_usecase_reproj_dask.ipynb**](notebooks/08_usecase_reproj_dask.ipynb) | **Dask Benchmark Use Case** | Benchmarking raster reprojection performance with and without Dask across different chunk sizes. |
