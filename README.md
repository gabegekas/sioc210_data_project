# Introduction:
GitHub repository for code associated with our SIOC 210 data project

## File Descriptions:

1. [test.py](https://github.com/gabegekas/sioc210_data_project/blob/main/scripts/test.py) - a test file

2. [global_temp.py]() - SST around the globe
3. [currents.py]() - global current vectors from buoy dispalcement (small time scale)
4. [correlation_heatmap.py]() - correlation heatmap of ocean physical properties and parameters
5. [temp_vs_depth.py]() - normalized temp vs depth plots
6. [temp_vs_abs(latitude).py]() - normalized temp vs latitude plots
7. [temp_vs_time_CA]() - CA coast temp vs time plots
8. [sal_vs_temp.py]() - salinity vs temperature plots
9. [temp_vs_latitude.py]() - plots the sea surface temperature vs the latitude

## Getting Started


### Dependencies:

1. [argopy](https://github.com/euroargodev/argopy) - can be installed with "pip install argopy" or conda
2. [matplotlib](https://matplotlib.org/) - can be installed with "pip install matplotlib" or conda
3. [numpy](https://numpy.org/) - can be installed with "pip install numpy" or conda
4. [cartopy](https://scitools.org.uk/cartopy/docs/latest/) - can be installed with "pip install cartopy" or conda
5. [Ipython](https://ipython.org/) - can be installed with "pip install Ipython" or conda
6. [scipy](https://scipy.org/) - can be installed with "pip install scipy" or conda
7. [seaborn](https://seaborn.pydata.org/) - can be installed with "pip install seaborn" or conda
8. [pandas](https://pandas.pydata.org/) - can be installed with "pip install pandas" or conda
9. Python3.9.x

### Installation

_Getting the code on your machine can be done in one step._

1. Clone the repo
   ```sh
   git clone https://github.com/gabegekas/sioc210_data_project.git
   ```


## Usage

_All the files are run in a similar manner._

- To generate the sea surface temperature plots on a global scale run:
    ```
    python global_temp.py
    ```


## Resources:

1. [Euro-Argo Github Page](https://github.com/euroargodev)
2. [Matplotlib Documentation](https://matplotlib.org/stable/users/index)
3. [Argopy Documentation](https://argopy.readthedocs.io/en/latest/)

## Data:
1. [Argo](https://argo.ucsd.edu/data/)


## Tasks:

### Coding:
- [x] Make private Github repository for easy group work
- [x] Figure out which modules would help us the most
- [ ] Data allocation (select datasets, write code to import data into best format to work with)
- [ ] Make cool visuals

### Presentation:
- [ ] Visualize data, look for trends
- [ ] Find best sections of data to focus on for the presentation
- [ ] Make slides and allocate presentation sections to team members