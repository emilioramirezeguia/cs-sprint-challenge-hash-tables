def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    dictionary = {}

    # if there's only 1 weight, return None
    if length == 1:
        return None

    # otherwise, loop through the weights and populate
    # the dictionary with the weight as the key and the index
    # as the value
    for i in range(length):
        dictionary[weights[i]] = i

    # loop through the weights again
    for weight in weights:
        # we're going to check whether this value is in the dictionary
        other_weight = limit - weight
        # if it is, that means two of our values equal our limit
        if other_weight in dictionary:
            # check which index is greater and return that one first
            if dictionary[weight] > dictionary[other_weight]:
                return (dictionary[weight], dictionary[other_weight])
            # if weights were repeated, only one dictionary entry was
            # created so hardcode the bigger index
            elif dictionary[weight] == dictionary[other_weight]:
                return (1, 0)
            else:
                return (dictionary[other_weight], dictionary[weight])

    return None

    # # brute-force solution O(n^2)
    # if length == 1:
    #     return None

    # for i in range(length - 1):
    #     for j in range(1, length):
    #         if weights[i] + weights[j] == limit:
    #             if i < j:
    #                 return (j, i)
    #             else:
    #                 return (i, j)

    # return None
