import plotter
import unittest
import os
import sys

### UNIT TESTS ###

class classTestUtils(unittest.TestCase):
    # setUp and tearDown
    @classmethod
    def setUpClass(cls):
        
        #what class variables can I use to test the output of visualizations? 
        
    @classmethod
    def tearDownClass(cls):
        cls.list_of_chars = None
        cls.list_of_ints = None
        cls.nested_L_ints = None
    
    def test_make_boxplot_filepath(self):
        # check to make sure the iris_csv file exists

        if plotter.make_boxplot('bad_file_path.csv'):        
            self.assertRaise(FileNotFoundError)

    
if __name__ == '__main__':
    unittest.main()