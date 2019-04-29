## Analyzing Cells in Confined Channels - Standardization of Fluorescence Intensity.
- This project focuses on implementing openCV and PIL modules in python to analyse microscopy images of cells in confined environments.
- This program, at the current milestone, parses an image of a cell and returns it's perimeter and centroid.
> Futher on from here, this result will be implemented in an attempt to standardize the fluoresence intensity of proteins in given cells. 

## Setup and Modules Required
- Python 3.7 is required. Program will not run well on Python 2.x due to difference in documentation of openCV and PIL. 
- PIL, numpy, openCV, matplotlib and time are required in order to run this program. 
- openCV can be installed by a pip install: `pip install openCV-python`

## How it works:
- The code reads in an image file and converts it into a binary image. 
- The binary images is parsed through several noise reduction filters.
- Multiple filters progressively reduce noise while making sure important features of the image are not lost. 
- Post noise reduction, the largest contour is extracted from the image.
- This contour is stored as a list of coordinates that constitue the cell boundary. 

## Making it all work:
- Clone the master and download the files locally.
- Once done, open `Final_Project.py`
- Go to the bottom and change the value of the variable `a` to be equal to the name of the image file that has to be analyzed, and then run the code.
