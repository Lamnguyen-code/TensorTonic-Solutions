def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    recall = 0
    precision = 0

    t = 0
    for i in range(k):
        if (recommended[i] in relevant): t += 1

    return [t / k, t / len(relevant)]