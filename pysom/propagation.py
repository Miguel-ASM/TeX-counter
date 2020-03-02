"""
Propagation of the wave functions
=================================

functions to propagate wave functions
"""

import numpy as np
from scipy import constants



def suzuki_trotter_step(psi, psip, expkin, V, nx, x, dx, px, dpx, dt):
    """
    Function that evolves a one-dimensional wave-function using a single step of the 2nd order Suzuki-Trotter
    """

    pi = np.pi
    hb = constants.hbar

    # First step of the SOM
    psip *= expkin
    psi[:] = nx*np.fft.ifft(psip*dpx)/(2*pi*hb) #inverse Fourier transform

    # Second step of the SOM
    psi *= np.exp(-1j*V*dt/hb)
    psip[:] = np.fft.fft(psi*dx)/(2*pi*hb) #Fourier transform

    # Last Step of the SOM
    psip *= expkin
    psi[:] = nx*np.fft.ifft(psip*dpx)/(2*pi*hb) #inverse transform

    #Normalize everything
    psi /= np.sqrt(np.trapz(np.absolute(psi)**2, x) )
    psip /= np.sqrt(np.trapz(np.absolute(psip)**2, px) )

    #This function returns nothing, is only updating the values of psi and psip


def suzuki_trotter(psi, psip, expkin, V, n, nx, x, dx, px, dpx, dt):
    """
    Function that evolves a one-dimensional wave-function using 2nd order Suzuki-Trotter
    """

    #Apply time evolution of step 'dt' for n times
    for i in range(n):
        suzuki_trotter_step(psi, psip, expkin, V, nx, x, dx, px, dpx, dt)

    #returns nothing, only updates values
