import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.array(x)
    y = np.array(y)

    return np.absolute(x - y).sum() * 1.0
    pass