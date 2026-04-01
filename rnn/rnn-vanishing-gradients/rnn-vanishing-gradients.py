import numpy as np

def compute_gradient_norm_decay(T: int, W_hh: np.ndarray) -> list:
    """
    Simulate gradient norm decay over T time steps.
    Returns list of gradient norms.
    """
    # YOUR CODE HERE
    n = np.linalg.norm(W_hh, ord = 2)
    res = []
    cur = 1.0
    for _ in range(T):
        res.append(cur) 
        cur *= n

    return res
    pass