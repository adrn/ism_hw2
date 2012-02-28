# Standard library
import os
import argparse
import logging

# Third-party
import matplotlib
matplotlib.use("Agg") # Hack to get my broken MPL to save a figure
import matplotlib.pyplot as plt
import numpy as np

# Used below to color output...don't touch!
_okColor = '\033[92m'
_errorColor = '\033[91m'
_ENDC = '\033[0m'

def readCloudyFile(filename):
    """ Reads in a CLOUDY .ovr file into a numpy recarray 
        
        The columns can then be accessed by doing arrayName.Htot, or
        whatever column you want (see the first line in a .ovr file)
    """
    return np.genfromtxt(filename, dtype=float, names=True, delimiter="\t").view(np.recarray)

def plotA(data):
    plt.plot(data.depth, data.eden/data.hden, 'k-', lw=2.)
    plt.xlabel(r"Depth [$cm$]")
    plt.ylabel(r"Fractional Ionization $x=n_e/n_H$")
    plt.savefig("Problem1_a.pdf")

def plotB(ovrData, emiData):
    idx = np.argsort(emiData.depth)
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(ovrData.depth, 10**ovrData.Te, 'k-')
    ax1.set_xlabel(r"Depth [$cm$]")
    ax1.set_ylabel(r"Temperature [$K$]")
    fig.savefig("Problem1_b_TvsD.pdf")
    
    fig = plt.figure()
    ax1 = fig.add_subplot(321)
    ax1.set_title("Ca B")
    ax1.plot(emiData.depth[idx], emiData.Ca_B__4861A[idx], 'k-', alpha=0.4, label=r"4861")
    ax1.plot(emiData.depth[idx], emiData.Ca_B__6563A[idx], 'k--', alpha=0.4, label=r"6563")
    ax1.legend(loc=3)
    ax1.set_ylabel(r"Emissivity [$log(erg$ $cm^{-3}$ $s^{-1})$]")
    ax1.set_ylim(-36., -20)
    
    ax2 = fig.add_subplot(322)
    ax2.set_title("[OIII]")
    ax2.plot(emiData.depth[idx], emiData.o__3__5007A[idx], 'k-', alpha=0.4, label=r"5007")
    ax2.plot(emiData.depth[idx], emiData.o__3__4959A[idx], 'k--', alpha=0.4, label=r"4959")
    ax2.plot(emiData.depth[idx], emiData.o__3__4931A[idx], 'k-.', alpha=0.4, label=r"4931")
    ax2.legend(loc=3)
    ax2.set_ylim(-36., -20)
    
    ax3 = fig.add_subplot(323)
    ax3.set_title("[OII] Doublet")
    ax3.plot(emiData.depth[idx], emiData.o_ii__3726A[idx], 'k-', alpha=0.4)
    ax3.set_ylabel(r"Emissivity [$log(erg$ $cm^{-3}$ $s^{-1})$]")
    ax3.set_ylim(-36., -20)
    
    ax4 = fig.add_subplot(324)
    ax4.plot(emiData.depth[idx], emiData.totl__4861A[idx], 'k-', alpha=0.4, label=r"totl 4861")
    ax4.plot(emiData.depth[idx], emiData.TOTL__4363A[idx], 'k--', alpha=0.4, label=r"totl 4363")
    ax4.legend(loc=3)
    ax4.set_ylim(-36., -20)
    
    ax5 = fig.add_subplot(325)
    ax5.set_title("[NII]")
    ax5.plot(emiData.depth[idx], emiData.n__2__5755A[idx], 'k-', alpha=0.4, label=r"5755")
    ax5.plot(emiData.depth[idx], emiData.n__2__6548A[idx], 'k--', alpha=0.4, label=r"6548")
    ax5.plot(emiData.depth[idx], emiData.n__2__6584A[idx], 'k--', alpha=0.4, label=r"6584")
    ax5.legend(loc=3)
    ax5.set_ylabel(r"Emissivity [$log(erg$ $cm^{-3}$ $s^{-1})$]")
    ax5.set_xlabel(r"Depth [$cm$]")
    ax5.set_ylim(-36., -20)
    
    ax6 = fig.add_subplot(326)
    ax6.set_title("[SII]")
    ax6.plot(emiData.depth[idx], emiData.s_ii__6716A[idx], 'k-', alpha=0.4, label=r"6716")
    ax6.plot(emiData.depth[idx], emiData.s_ii__6731A[idx], 'k--', alpha=0.4, label=r"6731")
    ax6.legend(loc=3)
    ax6.set_xlabel(r"Depth [$cm$]")
    ax6.set_ylim(-36., -20)
    
    fig.savefig("Problem1_b_LinevsD.pdf")

if __name__ == "__main__":
    
    if not os.path.exists("Problem1Data/test.ovr"):
        raise IOError("{0} not found! Did you run CLOUDY yet?".format("Problem1Data/test.ovr"))
    
    ovrData = readCloudyFile("Problem1Data/test.ovr")
    plotA(ovrData)
    
    emiData = readCloudyFile("Problem1Data/test.emi")
    plotB(ovrData, emiData)
    
    print emiData.dtype.names