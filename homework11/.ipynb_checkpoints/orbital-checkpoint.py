import numpy as np

# This is where my numpy orbital period function will live:

def new_orbital_period(a):
    period = np.sqrt(np.power(a, 3))
    return period