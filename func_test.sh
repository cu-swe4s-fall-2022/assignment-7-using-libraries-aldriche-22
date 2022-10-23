#!/bin/bash
###FUNCTIONAL TESTS###
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

#run the ssshtest script
. ssshtest

# RUN FUNCTIONAL TESTS FOR DATA_PROCESSOR
run get_random_matrix python data_processor.py
# wget -O iris.data \ 'https://github.com/cu-swe4s-fall-2022/assignment-7-using-libraries-aldriche-22/blob/main/iris.data'

#compare expected output with actual output
assert_in_stdout 1 
#return an exit code if expected and actual do not match
assert_exit_code 0

run get_file_dimensions python func.py
assert_in_stdout 1 
assert_exit_code 0

run write_matrix_to_file python func.py
assert_in_stdout 1 
assert_exit_code 0


# RUN FUNCTIONAL TESTS FOR PLOTTER
run make_iris_boxplot python func.py 
assert_in_stdout 1 
assert_exit_code 0

run make_iris_scatterplot python func.py 
assert_in_stdout 1 
assert_exit_code 0

run multi_panel python func.py 
assert_in_stdout 1 
assert_exit_code 0


