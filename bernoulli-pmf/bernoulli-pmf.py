import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    mean = p
    variance = p * (1 - p)
    x = np.array(x)
    f = x*p + (1 - x)*(1 - p)

    return (f, mean, variance)
    pass