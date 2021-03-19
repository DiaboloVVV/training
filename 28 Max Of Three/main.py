def main():
    userInput = str(input("Please give me 3 numbers after spaces\n")).split()
    if userInput[0] > userInput[1] and userInput[0] > userInput[2]:
        print(userInput[0])
    elif userInput[0] < userInput[1] and userInput[1] > userInput[2]:
        print(userInput[1])
    else:
        print(userInput[2])


if __name__ == '__main__':
    main()