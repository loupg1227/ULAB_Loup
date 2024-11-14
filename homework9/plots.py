# File name: Plots

import numpy as np
import matplotlib.pyplot as plt


def Plancks_law(min_wavelength, max_wavelength, temp): 
    """
    A few weeks ago in Astro class we did some stuff with Planck's law and graphs
    depending on wavelength and how temperature would change the spectral radiance
    of a star.

    Inputs:
    Minimum Wavelength: This will be the minimum value of our domain MUST BE IN NANOMETERS
    Maximum Wavelength: This will bether maximum value of our domain MUST BE IN MICROMETERS
    Temperature: This whole function depends on temperature, so this is our main input

    Outputs: 
    A graph of Planck's radiation law.
    """
    
    Spectrum = [] # This will be our Y values and what we will graph. 
    h = 6.626 * 10**-34
    c = 3 * 10**8
    k = 1.38 * 10**-23
    
    x = np.linspace((min_wavelength * 10**-9), (max_wavelength * 10**-6), 1000) 
    wavelength = np.array(x) # This is how we convert our top and bottom domain constrictions to wavelengths that we will plug into our equations as inputs. This will also serve as the inputs for the graph as the X-values.
    
    for i in wavelength:
        numerator = (2 * h * (c**2)) / i**5
        denominator = (np.e**((h * c) / (i * k * temp)) -1)
        final = numerator / denominator 
        Spectrum.append(final) # This is the brunt of the code, this is the part that does all the calculations for us. 

    x_values = wavelength
    y_values = Spectrum

    plt.figure(figsize=(10,6))
    plt.gca().set_facecolor('black') # This is my "personal touch" where I really like the way this looks which is why I add it :)
    
    plt.plot(x_values, y_values, color='white', linestyle="-", label="Planck's Law")
    plt.title("Planck's Radiation Law")
    plt.xlabel("Wavelength (meter)")
    plt.ylabel("Spectral Radiance")
    plt.legend()
    plt.show()





