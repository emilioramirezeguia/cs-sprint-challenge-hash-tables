def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # dictionary = {}
    # for i in range(length):
    #     if weights[i] not in dictionary:
    #         dictionary[weights[i]] = i
    # return dictionary
    if length == 1:
        return None

    for i in range(length - 1):
        for j in range(1, length):
            if weights[i] + weights[j] == limit:
                if i < j:
                    return (j, i)
                else:
                    return (i, j)

    return None


# testing
# weights_3 = [4, 6, 10, 15, 16]
# answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
# print(answer_3)
weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
print(answer_2)
