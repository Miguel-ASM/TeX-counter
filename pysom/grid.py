"""
Definition of a position/momentum grid
======================================

functions to define the position/momentum grid
"""

import numpy as np
from scipy import constants

def grid_def(nx, Lx0, Lx, hb):
    """
    Function that defines a fixed one-dimensional grid for momentum and position
    """

    pi = np.pi
    hb = constants.hbar

    dx = Lx/(nx-1)                              #size of the step in x
    x = np.linspace(Lx0, Lx0+Lx, nx)

    dpx = 2*np.pi*hb/(nx*dx)                    #size of the step in the position
    px = dpx*np.arange(nx/2+1)
    px = np.concatenate((px[:-1],-px[-1:0:-1])) #definition of the momentum

    return x, dx, px, dpx
