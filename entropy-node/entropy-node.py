import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if (len(y) == 0): return 0.0 # empty
        
    cnt = dict([])
    S = set([])

    # compute frequency of each elements in y
    for i in y: 
        if i not in S:
            S.add(i)
            cnt[i] = 1
        else:
            cnt[i] += 1

    entropy = 0.0
    l = len(y)
    for i in S:
        p = cnt[i] / l # probaility of i
        entropy -= p*np.log2(p)

    print(entropy)
    return entropy
    pass