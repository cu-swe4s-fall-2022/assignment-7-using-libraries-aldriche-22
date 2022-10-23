#!/bin/bash

set -e
set -u
set -o pipefail 

python3 data_processor.py

python3 plotter.py --file_name 'iris.data'


#test scripts with pycodestyle
# pycodestyle plotter.py 
# pycodestyle test_data_processor.py 

#run unit tests
# python3 test_data_processor.py 
# python3 test_plotter.py

#run functional tests
# bash func_test.sh