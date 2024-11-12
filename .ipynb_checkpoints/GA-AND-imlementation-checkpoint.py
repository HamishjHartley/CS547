import numpy as np
import random

def load_data(file_path):
    """
    Load test case data from a file. Each row in the file should contain:
    - binary values representing faults detected by each test.
    - the final value is the execution time for the test.
    """
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            values = list(map(int, line.strip().split()))
            faults = values[:-1]
            time = values[-1]
            data.append((faults, time))
    return data

# Load both datasets

with open('C:/Users/theha/OneDrive/Documents/repos/CS547/newbigfaultmatrix.txt') as small_data: lines = f.readlines()


