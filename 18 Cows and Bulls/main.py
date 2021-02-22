import random as rand


def main():
    compNumb = str(rand.randint(1000, 9999))
    guesses = 1
    while True:
        userNumb = str(input("Please select a 4 digit number"))
        cow = 0
        bull = 0
        if userNumb == 'exit':
            break
            print(f"You guessed {guesses} times")
        for j in range(0, 4):
            if compNumb[j] == userNumb[j]:
                cow += 1
        if cow != 4:
            for i in range(0, 4):
                if compNumb[i] in userNumb:
                    bull += 1
            print(f"You have {cow} cows and {bull} bulls")
        else:
            print(f"Congratulations you guessed number {compNumb} in {guesses} tries")
            guesses = 1
            compNumb = str(rand.randint(1000, 9999))
    return 0


if __name__ == '__main__':
    main()
