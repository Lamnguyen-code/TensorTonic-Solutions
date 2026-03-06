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
        # z = np.array([X[i].dot(w) for i in range(n)]) + b
        z = w.dot(X.T) + b
        print(z.shape)
        
        grad_z = _sigmoid(z) - y
        # print(f"{grad_z.shape}, {X.shape}")
        
        # grad_w = (grad_z * X).sum() * 1.0 / n
        # grad_w = X.T.dot(grad_z) * 1.0 / n
        grad_w = grad_z.dot(X) / n
        grad_b = grad_z.sum() / n
        # print(grad_w.shape)
        # print(grad_b)

        w -= lr * grad_w
        b -= lr * grad_b

    print("Done")
    print(w.shape)
    print(b.shape)
    
    return (w, b)
    pass