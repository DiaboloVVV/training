def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # print([aa for aa in a if aa<5])
    aa = []
    inpu = int(input("Number?"))
    for i in a:
        if i < inpu:
            aa.append(i)
    print(aa)


if __name__ == "__main__":
    main()
