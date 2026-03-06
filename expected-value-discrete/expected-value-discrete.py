import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    t = 0.0
    for p_i in p:
        t += p_i

    eps = 10e-6
    
    if (abs(t - 1) > eps): raise ValueError("ValueError")
    # Write code here
    e = 0.0
    for i in range(len(x)):
        e += x[i] * p[i]

    return e
    pass
