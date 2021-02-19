import random as ran


def main():
    guesses = 1
    numb = str(ran.randint(1, 9))
    while True:
        ex = input("Guess the number!\n")
        print(numb)
        if ex == "exit":
            break
        else:
            if ex > numb:
                print("Number is lower!\n")
                guesses += 1
            elif ex < numb:
                print("Number is greater!\n")
                guesses += 1
            else:
                print(f"Congratulations you guessed the number {numb} in {guesses} tries")
                guesses = 1
                numb = str(ran.randint(1, 9))


if __name__ == "__main__":
    main()
