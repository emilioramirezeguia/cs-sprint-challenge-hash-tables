def has_negatives(a):
    """
    YOUR CODE HERE
    """
    positives = {}
    negatives = {}
    result = []

    for i in range(len(a)):
        if a[i] >= 0:
            if a[i] not in positives:
                positives[a[i]] = 0
            else:
                positives[a[i]] = 0
        else:
            if a[i] not in negatives:
                negatives[a[i]] = 0

    for key in positives:
        if -key in negatives:
            result.append(key)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
