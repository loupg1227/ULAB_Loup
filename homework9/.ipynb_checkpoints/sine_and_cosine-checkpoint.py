# File name = sine and cosine

import numpy as np
import matplotlib.pyplot as plt

def cosine_and_sine_horizontal(start, end):
    """
    This function will take in the start and the end of a certain domain and output the graphs of 
    sine and cosine.

    Inputs:
    Start of domain
    End of domain

    Outputs:
    2 subplots, side by side, of both sine and cosine
    """
    
    inputs = np.linspace(start, end, 1000)
    
    figure, axs = plt.subplots(1, 2, figsize=(12,6)) # This will create 2 subplots, with one row and 2 columns, so both figures will be side by side.

    axs[0].set_facecolor('black')
    axs[0].plot(inputs, np.sin(inputs), color='white', label='sin(x)')
    axs[0].set_title('Plot of Sin(x)')
    axs[0].set_xlabel('Inputs')
    axs[0].set_ylabel('Sin(x)')
    axs[0].legend()

    # Now we make our second graph, which is cosine.
    
    axs[1].plot(inputs, np.cos(inputs), color='black', label='cos(x)')
    axs[1].set_title('Plot of Cos(x)')
    axs[1].set_xlabel('Inputs')
    axs[1].set_ylabel('Cos(x)')
    axs[1].legend()

    plt.show

# Now we will make the same function, but all we change is the dimension of the subplots.

def cosine_and_sine_vertical(start, end):
    """
    This function will take in the start and the end of a certain domain and output the graphs of 
    sine and cosine.

    Inputs:
    Start of domain
    End of domain

    Outputs:
    2 subplots, side by side, of both sine and cosine
    """
    
    inputs = np.linspace(start, end, 1000)
    
    figure, axs = plt.subplots(2, 1, figsize=(12,12)) # This is the only line that will change, because we now make 2 rows and one column, and we change the figure size so that they don't impose on each other

    axs[0].set_facecolor('black')
    axs[0].plot(inputs, np.sin(inputs), color='white', label='sin(x)')
    axs[0].set_title('Plot of Sin(x)')
    axs[0].set_xlabel('Inputs')
    axs[0].set_ylabel('Sin(x)')
    axs[0].legend()

    # Now we make our second graph, which is cosine.
    
    axs[1].plot(inputs, np.cos(inputs), color='black', label='cos(x)')
    axs[1].set_title('Plot of Cos(x)')
    axs[1].set_xlabel('Inputs')
    axs[1].set_ylabel('Cos(x)')
    axs[1].legend()

    plt.show
















