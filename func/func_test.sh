#!/bin/bash
###FUNCTIONAL TESTS###
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

#run the ssshtest script
. ssshtest

# wget -O iris.data \ 'https://github.com/cu-swe4s-fall-2022/assignment-7-using-libraries-aldriche-22/blob/main/iris.data'

# RUN FUNCTIONAL TESTS FOR PLOTTER
run test_plotter python plotter.py --file_name '../iris.data'
assert_no_stdout
assert_exit_code 0




