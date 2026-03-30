import numpy as np

def rnn_cell(x_t: np.ndarray, h_prev: np.ndarray, 
             W_xh: np.ndarray, W_hh: np.ndarray, b_h: np.ndarray) -> np.ndarray:
    """
    Single RNN cell forward pass.
    """
    # YOUR CODE HERE
    tmp = h_prev @ W_hh.T + x_t @ W_xh.T + b_h
    return np.sinh(tmp) / np.cosh(tmp)

def rnn_forward(X: np.ndarray, h_0: np.ndarray,
                W_xh: np.ndarray, W_hh: np.ndarray, b_h: np.ndarray) -> tuple:
    """
    Forward pass through entire sequence.
    """
    # YOUR CODE HERE
    h_prev = h_0
    h = []
    times = X.shape[1]
    for t in range(times):
        x_t = X[:, t, :]
        h.append(rnn_cell(x_t, h_prev, W_xh, W_hh, b_h)) 
        h_prev = h[-1]

    h_final = h[-1]
    h = np.stack(h, axis = 1)
    return (h, h_final)
    pass

