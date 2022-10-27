# libraries v1.0
# Purpose of the software
Data_processor.py uses the numpy library to develop functions for processing matrices, including building a matrix based on desired dimensions, finding the dimensions of a matrix in a .csv file, and writing a matrix to a file. Plotter.py uses the matplotlib library to visualize iris data. 

## data_processor.get_random_matrix
Builds an array of floating point numbers between (0,1], dimensions defined by num_rows and num_columns.

## data_processor.get_file_dimensions
Takes in the name for a comma separated value (csv) file. Reads the file and returns the dimensions of the tabular data (rows, columns).

## data_processor.write_matrix_to_file
Creates an N x M matrix of random numbers from a uniform distribution in the range of (0,1] and then write it to a csv file.

## plotter.py
Reads the iris.data csv, generates a boxplot, generates a scatterplot, and combiens the boxplot and scatterplot into a multi panel visualization.


# How to use the software
Execute run.sh as a bash script. Unit tests are found in test/test_data_processor.py and functional tests are found in func/test_func.sh. Tests for pycodestyle are currently commented out in the run.sh.  

# How to install the software
This software requires matplotlib, numpy and pandas installation.

To install the dependencies needed, run in the terminal:
$ conda env create -f environment.yml

To download iris.data, uncomment the wget (line 8) in test_func.sh. 

