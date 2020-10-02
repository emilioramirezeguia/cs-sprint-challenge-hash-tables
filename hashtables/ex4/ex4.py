def has_negatives(a):
    """
    YOUR CODE HERE
    """
    dictionary = {}
    result = []

    for i in range(len(a) - 1):
        if a[i] >= 0 and a[i + 1] < 0:
            if a[i] not in dictionary:
                dictionary[a[i]] = a[i + 1]
            else:
                dictionary[a[i]] = a[a + 1]
    print(dictionary)
    for key in dictionary:
        result.append(key)

    return result


# if __name__ == "__main__":
#     print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
print(has_negatives([1, 2, 3]))
print(has_negatives([1, 2, 3, -4]))
print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
