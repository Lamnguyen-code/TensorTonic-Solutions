import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    w = np.zeros(X[0].shape)
    b = 0.0
    n = len(y)
    
    for s in range(steps):
        z = w.dot(X.T) + b
        
        grad_z = _sigmoid(z) - y
        
        grad_w = grad_z.dot(X) / n
        grad_b = grad_z.sum() / n

        w -= lr * grad_w
        b -= lr * grad_b

    
    return (w, b)
    pass