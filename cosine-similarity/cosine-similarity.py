import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)

    a_a = np.sqrt((a**2).sum())
    a_b = np.sqrt((b**2).sum())

    if (a_a * a_b == 0): return 0

    return a.dot(b) / (a_a * a_b)
    pass