#File: even_sum.py

import numpy as np

def sum_even_numbers(numbers):
    """
    Return the sum of all even numbers
    in a given list of array
    """
    sum = np.sum(num for num in numbers if num % 2 == 0)
    return sum