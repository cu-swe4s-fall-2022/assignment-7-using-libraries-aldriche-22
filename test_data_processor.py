import unittest
import numpy as np
import pandas as pd
import os
import sys
import data_processor as dp 
import random

# Unit tests for data_processor

class classTestUtils(unittest.TestCase):
    # setUp and tearDown
    @classmethod
    def setUpClass(cls):
        # cls.x = None
        # cls.y = None
        # while cls.x != 0:
        #     cls.x =  random.random()
        # while cls.y != 0:
        #     cls.y =  random.random()
        
        # cls.x = random.random()
        # cls.y = random.random()
        # having issues with the nonzero criteria, going to come back to this 
        cls.x = 2
        cls.y = 3
        cls.matrix = dp.get_random_matrix(cls.x, cls.y)
        
        # generate a practice csv file 
        practice_array = np.array([[1,2],[3,4]])
        np.savetxt("use_for_test_get_file_dimensions.csv", practice_array, delimiter=",")
        
        
    @classmethod
    def tearDownClass(cls):
        cls.x = None
        cls.y = None
        cls.matrix = None
    
    def test_get_random_matrix(self):
        # positive test: test that the the matrix is the correct dimensions

        self.assertEqual(len(self.matrix), self.x)
        self.assertEqual(len(self.matrix[0]), self.y)


        # negative test: like the positive test, but swaps rows and columns 
        self.assertNotEqual(len(self.matrix), self.y)
        self.assertNotEqual(len(self.matrix[0]), self.x)

        # check that num_rows and num_columns are non-zero
        self.assertNotEqual(len(self.matrix), 0) 

    def test_get_file_dimensions(self):
        # positive test: test that the output of the function matches the 
        # dimensions of the matrix
        self.assertEqual(dp.get_file_dimensions('use_for_get_file_dimensions.csv'), 
                         (cls.x, cls.y))
    
    # wondering about syntax here: 
    # def test_get_file_dimensions_file_path(self): 
    #     if dp.get_file_dimensions('bad_file_path.csv'):        
    #         self.assertRaise(FileNotFoundError)
    
    

    def test_write_matrix_to_file(self):
        # test that the dimensions are what I think they are (reuse test from get_random_matrix)
        self.assertEqual(len(self.matrix), self.x)
        self.assertEqual(len(self.matrix[0]), self.y)
        
        # test that the output csv can be read and is the right dimensions
        dp.write_matrix_to_file(cls.x, cls.y, 'test_write_matrix_to_file.csv')
        df = pd.read_csv('test_write_matrix_to_file.csv', sep=',', header = None)
        self.assertEqual(len(df), self.x)
        self.assertEqual(len(df[0]), self.y)
        

if __name__ == '__main__':
    unittest.main()
