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
        cls.x =  random.randint(1,100)
        cls.y =  random.randint(1,100)

        # generate a practice csv file 
        practice_array = np.array([[1,2],[3,4]])
        np.savetxt("use_for_test_get_file_dimensions.csv", practice_array, delimiter=",")
        
    @classmethod
    def tearDownClass(cls):
        cls.x = None
        cls.y = None
        cls.matrix = None
    
    def test_get_random_matrix(self):
        matrix = dp.get_random_matrix(self.x, self.y)
        # positive test: test that the the matrix is the correct dimensions
        self.assertEqual(len(matrix), self.x)
        self.assertEqual(len(matrix[0]), self.y)


         # negative test: like the positive test, but swaps rows and columns 
        self.assertNotEqual(len(matrix), self.y)
        self.assertNotEqual(len(matrix[0]), self.x)

         # check that num_rows and num_columns are non-zero
        self.assertNotEqual(len(matrix), 0) 

    def test_get_file_dimensions(self):
        # positive test: test that the output of the function matches the 
        # dimensions of the matrix
        self.assertEqual(dp.get_file_dimensions('use_for_test_get_file_dimensions.csv'), 
                         (1,2))

    def test_write_matrix_to_file(self):
        # test that the output csv can be read and is the right dimensions
        dp.write_matrix_to_file(self.x, self.y, 'test_write_matrix_to_file.csv')
        df = pd.read_csv('test_write_matrix_to_file.csv', sep=',', header = None)
        self.assertEqual(len(df), self.x)
        self.assertEqual(len(df[0]), self.x)
        
if __name__ == '__main__':
    unittest.main()
