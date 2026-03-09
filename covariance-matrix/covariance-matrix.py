import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.array(X)

    if (X.ndim != 2 or X.shape[0] < 2): # invalid cases 
        return None

    X = X - X.mean(axis = 0)

    return X.T.dot(X) / (X.shape[0] - 1)
    pass