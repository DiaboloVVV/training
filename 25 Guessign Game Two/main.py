def main():
    tries = 1
    startNumb = 50
    userNumber = int(input())
    print("I guess it's number... {}".format(startNumb))
    while True:
        if startNumb == userNumber:
            print("I guessed your number ({}) in {} tries!".format(userNumber, tries))
            break
        else:
            user = str(input("Is your number higher or lower than mine?"))
            if startNumb == userNumber:
                print("I guessed your number ({}) in {} tries!".format(userNumber, tries))
                break
            elif user == "lower":
                startNumb -= 1
                print("I guess it's number... {}".format(startNumb))
                tries += 1
            elif user == "higher":
                startNumb += 2
                print("I guess it's number... {}".format(startNumb))
                tries += 1
            else:
                print("Don't know")
    return 0


if __name__ == '__main__':
    main()
