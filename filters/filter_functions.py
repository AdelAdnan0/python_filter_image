import numpy as np

def mean(matrix):
    """Calculate the mean of the values in the matrix."""
    total_sum = np.sum(matrix)
    count = matrix.size
    return total_sum / count if count != 0 else 0

def median(matrix):
    """Calculate the median of the values in the matrix."""
    flat_list = matrix.flatten()
    flat_list.sort()
    n = len(flat_list)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 0:
        return (flat_list[mid - 1] + flat_list[mid]) / 2
    else:
        return flat_list[mid]
