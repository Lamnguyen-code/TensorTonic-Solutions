import numpy as np

def is_2d_list(x):
    return isinstance(x, list) and all(isinstance(row, list) for row in x) and len(x) > 0

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
        
    if (is_2d_list(matrix) and (len(matrix[0]) > 0)):
        for i in range(len(matrix) - 1):
            if (len(matrix[i]) != len(matrix[i + 1])): return None
    else: return None
                
    matrix = np.array(matrix)
    if (matrix.shape[0] != matrix.shape[1]): # invalid cases
        return None

    eigenvalues = np.linalg.eigvals(matrix)
    return np.sort_complex(eigenvalues)
    pass