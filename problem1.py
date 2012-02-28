# Standard library
import os
import argparse
import logging

# Third-party
import matplotlib.pyplot as plt
import numpy as np

# Used below to color output...don't touch!
_okColor = '\033[92m'
_errorColor = '\033[91m'
_ENDC = '\033[0m'



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, dest="filename", default="",
        				help="The filename of the output file you want to plot.")
    
    args = parser.parse_args()
    
    # If the user forgot to specify a filename, let them know!
    if args.filename == "":
        logging.error("{0}You have to specify a filename using the '-f' flag when running this script!{1}".format(_errorColor, _ENDC))
        raise AttributeError("Invalid filename.")
        
    # If the file they specified doesn't exist, throw a tantrum
    if not os.path.exists(args.filename):
        raise ValueError("{1}The file you specified doesn't exist:{2} {3}{0}{4}".format(args.filename, _errorColor, _ENDC, _okColor, _ENDC))
    
    plotCloudyOutput(args.filename)