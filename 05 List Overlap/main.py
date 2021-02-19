import random

def main(a,b):
    bLength = len(b)
    aLength = len(a)
    final = []
    if (bLength > aLength):
        for elem in b:
            if elem in a:
                final.append(elem)
    else:
        for elem2 in a:
            if elem2 in b:
                final.append(elem2)
    final = list(set(final))
    print(final)


def randomFunction():
    userInput = int(input("Give range nr.1\n"))
    userInput2 = int(input("Give range nr.2\n"))
    basicList = []
    basicList2 = []
    for elem in range(userInput):
        # print(f"number {elem+1} {random.randint(1,userInput)}")
        b = random.randint(1, userInput)
        basicList.append(b)
    for elem in range(userInput2):
        c = random.randint(1, userInput)
        basicList2.append(c)
    print(basicList, "\n", basicList2)
    main(basicList, basicList2)


if __name__ == "__main__":
    randomFunction()
