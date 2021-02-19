def loopfunction():
    c = [1, 1, 2, 3, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    d = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    e = []
    for elem in c:
        # if elem in e:
        #     continue
        if elem in d and elem not in e:
            e.append(elem)
    return e


def setfunction():
    a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
    b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    print(a & b)
    print(loopfunction())


if __name__ == "__main__":
    setfunction()
