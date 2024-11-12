import numpy as np
import random

def parse_fault_matrix(file_path):
    with open(file_path, 'r') as file:
        fault_matrix = []
        for line in file:
            parts = line.strip().split(',')
            test_id = parts[0]
            faults = list(map(int, parts[1:]))
            fault_matrix.append((test_id, faults))
    return fault_matrix

# Main execution
if __name__ == "__main__":
    # Load the fault matrix data
    fault_matrix = parse_fault_matrix(r'smallfaultmatrixplustime.txt')
    print(fault_matrix)

