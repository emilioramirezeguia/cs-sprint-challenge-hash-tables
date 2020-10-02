def intersection(arrays):
    """
    YOUR CODE HERE
    """
    dictionary = {}
    result = []

    for array in arrays:
        for num in array:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1

    for key in dictionary:
        if dictionary[key] == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
