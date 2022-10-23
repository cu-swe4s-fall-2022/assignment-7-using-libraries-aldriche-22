import data_processor as dp
import plotter
import sys
import random



dp_func = sys.argv[1]
plot_type = sys.argv[2]

def main():
    # FUNCTIONAL TESTS FOR DATA PROCESSOR
    # need practice array to test with 
    # how should func tests be different from unit tests here? 
    
    if dp_func == 'get_random_matrix':
        
    elif dp_func == 'get_file_dimensions':

    elif dp_func == 'write_matrix_to_file':
        
    else: 
        print("dp_func should be a function in data_processor, either \ 
        'get_random_matrix', 'get_file_dimensions' or 'write_matrix_to_file'"
    
    
    # FUNCTIONAL TESTS FOR PLOTTER
    
    if plot_type == 'boxplot':
        # test expected output? How to quantify stdout? and sys.exit? 
                        
    elif plot_type == 'scatterplot':
    
        
    elif plot_type == 'multi_panel':
        
        
    else:
        print("plot_type should be a function in plotter, either 'boxplot', 
              'scatterplot' or 'multi_panel'")