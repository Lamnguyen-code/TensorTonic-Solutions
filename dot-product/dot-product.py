import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    if (len(x) != len(y)): raise ValueError("ValueError") # length mismatch
        
    x = np.array(x)
    y = np.array(y)

    return x.dot(y) * 1.0
    pass