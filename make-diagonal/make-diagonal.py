import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    v = np.array(v)
    I = np.identity(n = v.shape[0],  dtype = v.dtype)
    return I * v
    pass
