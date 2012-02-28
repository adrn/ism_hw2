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

def plotCloudyOutput(filename):
    """ Given a .con output file from CLOUDY, produce a
        matplotlib plot assuming wavelength data in microns
    
    """
    data = np.genfromtxt("pn.con", usecols=[0,6], dtype=[("wavelength", float), ("emission", float)])
    data = data.view(np.recarray)
    
    plt.loglog(data.wavelength, data.emission, 'k-', linewidth=1)
    plt.xlim(1E-1, 1E3)
    plt.ylim(1E-3, 1E3)
    plt.xlabel(r"Wavelength [$\mu m$]")
    plt.ylabel(r"$\nu f_\nu$ [$erg$ $cm^{-2}$ $s^{-1}$]")
    plt.show()

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