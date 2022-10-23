import numpy as np
import pandas as pd
import sys

def get_random_matrix(num_rows, num_columns):
    '''
    Description:
    Builds an array of floating point numbers between (0,1], dimensions defined by
    num_rows and num_columns
    
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
            # need to incorporate random seed to ensure reproducibility!!
            matrix = np.random.rand(num_rows, num_columns)
            print(matrix)
        except: 
            raise Exception('dimensions of array must be nonzero')

            
def get_file_dimensions(file_name):
    '''
    Description:
    Takes in the name for a comma separated value (csv) file. Reads the file 
    and returns the dimensions of the tabular data (rows, columns)

    Input:
    file_name: str
        name of a csv file to check the dimensions
        
    Outputs:
    rows_cols: tuple
        number of rows and columns (r, c)
    '''
    file = None 
    try: 
        file = pd.open_csv(file_name)
        df = pd.Dataframe(file)
        rows = len(df.axes[0])
        cols = len(df.axes[1])
        rows_cols = (rows, cols)
        print(rows_cols)
        
        # could also use np.shape(df)
        
    except: 
        FileNotFoundError
        sys.exit(1)

def write_matrix_to_file(num_rows, num_columns, file_name):
    '''
    Description:
    Creates an N x M matrix of random numbers from a uniform distribution in the 
    range of (0,1] and then write it to a csv file.
    Inputs:
    num_rows: int > 0
        number of rows in the matrix
    num_columns: int > 0
        number of columns in the matrix
    file_name: str
        name of a csv file to save the matrix in
    
    '''
    if num_rows != 0 and num_columns != 0:
        try:
            matrix = np.random.rand(num_rows, num_columns)
            np.savetxt(file_name, matrix, delimiter=",")
        except: 
            raise Exception('dimensions of array must be nonzero')
    
    