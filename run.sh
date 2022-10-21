#!/bin/bash

set -e
set -u
set -o pipefail 


python3 data_processor.py --x 4 \
                          --y 5



#test scripts with pycodestyle
# pycodestyle plotter.py 
# pycodestyle test_data_processor.py 


#run unit tests
python3 test_data_processor.py 

#run functional tests
