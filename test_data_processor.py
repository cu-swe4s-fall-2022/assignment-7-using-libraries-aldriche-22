import unittest
import os
import sys
import data_processor as dp 
import random

# Unit tests for data_processor

class classTestUtils(unittest.TestCase):
    # setUp and tearDown
    @classmethod
    def setUpClass(cls):
        
        cls.x =  random.randint(0, 10)
        cls.y =  random.randint(0, 10)
        cls.matrix = dp.get_random_matrix(x,y)
        
    @classmethod
    def tearDownClass(cls):
        cls.x = None
        cls.y = None
        cls.matrix = None
    
    def get_random_matrix(self):
    # positive test: test that the the matrix is the correct dimensions

        self.assertEqual(len(self.matrix), self.x)
        self.assertEqual(len(self.matrix[0]), self.y)


        # negative test: like the positive test, but swaps rows and columns 
        self.assertNotEqual(len(self.matrix), self.y)
        self.assertNotEqual(len(self.matrix[0]), self.x)

if __name__ == '__main__':
    unittest.main()