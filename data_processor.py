# remember to import your libraries!
import numpy as np


#TODO
'''
In the file data_processor.py, create a function called get_random_matrix(). This function
should create and return an N x M matrix of random floating point numbers sampled from a uniform in
the range of (0,1] (hint checkout numpy.random.rand()).
Input parameters:
a. num_rows : number of rows, integer > 0
b. num_columns : number of columns, integer > 0
Return 2-dimensional numpy array
'''


def get_random_matrix(num_rows, num_columns):
    '''
    Inputs:
    num_rows: int
        number of rows in the matrix
    num_columns: int
        number of columns in the 2D matrix
        
    Outputs:
    matrix: array of dimensions defined by num_rows, num_columns
    '''
    if num_rows != 0 and num_columns != 0:
        try:
            matrix = np.random.uniform(num_rows, num_columns)
            print(matrix)
        except: 
            raise Exception('dimensions of array must be nonzero')

def get_file_dimensions(file_name):
    return (0,0)

def write_matrix_to_file(num_rows, num_columns, file_name):
    return None
