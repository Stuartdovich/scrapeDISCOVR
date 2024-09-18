
# scrapeDISCOVR

## Overview
This project involves a web scraping script designed to retrieve solar wind and magnetic field data from the DISCOVR satellite. The data is used in real-time to update a model predicting the induced electric field, based on parameters such as solar wind density, speed, and the magnetic field strength (Bt).

The model is derived from the paper "[Regression-based forecast model of induced geoelectric field](http://onlinelibrary.wiley.com/doi/10.1002/2016SW001518/full)." It provides an empirical method for predicting the upper envelope of induced electric field components using solar wind plasma and magnetic field measurements.

## Features
- **Real-time data update**: Fetches solar wind and magnetic field data every minute.
- **Predicts induced electric field**: Uses solar parameters to calculate components of the electric field.
- **Visualization**: Real-time plotting of the electric field predictions.

## How It Works
1. The script fetches real-time data from the following sources:
   - **Magnetic field data**: [NOAA Solar Wind Magnetic Field (5-minute)](http://services.swpc.noaa.gov/products/solar-wind/mag-5-minute.json)
   - **Plasma data**: [NOAA Solar Wind Plasma (5-minute)](http://services.swpc.noaa.gov/products/solar-wind/plasma-5-minute.json)

2. It extracts the following parameters:
   - **Bt**: Total magnetic field strength
   - **Vsw**: Solar wind speed
   - **Roh**: Solar wind density

3. The script calculates the dynamic pressure (Pd) and computes the induced electric field components \(E_{\chi}\) and \(E_{\gamma}\) using the following regression-based equations:
   - \(E_{\chi} = 0.06 \cdot (Pd - P_{d-10})^{0.38} \cdot Bt^{0.39} \cdot Vsw^{0.51} - 0.53\)
   - \(E_{\gamma} = 0.06 \cdot (Pd - P_{d-10})^{0.58} \cdot Bt^{0.38} \cdot Vsw^{0.55} - 0.85\)

4. Data is appended to arrays and visualized in real-time, updating every minute.

## Dependencies
- **Python 3.x**
- **NumPy**: For numerical calculations and data handling.
- **Matplotlib**: For real-time plotting and animation.
- **Json**: To parse the fetched data.
- **Urllib2**: To make web requests.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/scrapeDISCOVR.git
   ```

2. Install the required Python libraries:
   ```bash
   pip install numpy matplotlib
   ```

3. Run the script:
   ```bash
   python scrapeDISCOVR.py
   ```

## Usage
Once the script is running, it will fetch and display real-time predictions of the induced electric field based on the latest solar wind and magnetic field data. The plot will automatically update every 60 seconds.

## Citation
If you use this script or data in your research, please cite the original paper:

**Love, J. J., et al.** "Regression-based forecast model of induced geoelectric field." *Space Weather* 15.9 (2017): 1215-1231. [DOI: 10.1002/2016SW001518](http://onlinelibrary.wiley.com/doi/10.1002/2016SW001518/full)

