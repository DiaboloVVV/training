def main():
    userInput = int(input("Gimme your number to divide:\n"))
    numberRange = list(range(1, userInput+1))

    dividors = []
    for e in numberRange:
        if userInput % e == 0:
            dividors.append(e)
    print(dividors)


if __name__ == "__main__":
    main()
