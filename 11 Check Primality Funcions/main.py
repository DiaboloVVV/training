def prime(numb):
    div = list(range(1, numb+1))
    divList = []
    for e in div:
        if numb % e == 0:
            divList.append(e)
    if len(divList) == 2:
        return True
    else:
        return False


def main():
    numb = int(input("Gimme number "))
    print(prime(numb))


if __name__ == "__main__":
    main()
