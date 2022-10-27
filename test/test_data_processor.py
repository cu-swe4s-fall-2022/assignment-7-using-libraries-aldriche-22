import unittest
import data_processor as dp 
import random
import numpy as np
import pandas as pd

# Unit tests for data_processor

class classTestDataProcessor(unittest.TestCase):
    # setUp and tearDown
    @classmethod
    def setUpClass(cls):
        
        cls.x =  random.randint(1, 100)
        cls.y =  random.randint(1, 100)
        cls.matrix = dp.get_random_matrix(cls.x, cls.y)
        
        practice_array = np.array([[1,2], [3,4]])
        np.savetxt('use_for_test_get_file_dimensions.csv', practice_array, delimiter=",")
        
    @classmethod
    def tearDownClass(cls):
        cls.x = None
        cls.y = None
        cls.matrix = None
    
    def test_get_random_matrix(self):
        # positive test: test that the the matrix is the correct dimensions

        self.assertEqual(len(self.matrix), self.x)
        self.assertEqual(len(self.matrix[0]), self.y)

        # negative test: test if value is not in list, return -1
        self.assertNotEqual(len(self.matrix), self.y)
        self.assertNotEqual(len(self.matrix[0]), self.x)
    
    def test_get_file_dimensions(self):
        self.assertEqual(dp.get_file_dimensions('use_for_test_get_file_dimensions.csv'), (1,2))
        
        # negative test for a bad file path 
        # self.assertRaises(FileNotFoundError, dp.get_file_dimensions, 'bad_file_path')
    
    def test_write_matrix_to_file(self):
        dp.write_matrix_to_file(self.x, self.y, 'test_write_matrix_to_file.csv')
        df = pd.read_csv('test_write_matrix_to_file.csv', sep=',', header=None)
        self.assertEqual(len(df), self.x)
        self.assertEqual(len(df[0]), self.x)
        

if __name__ == '__main__':
    unittest.main()