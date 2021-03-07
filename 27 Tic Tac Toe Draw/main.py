def main():
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    x = 0
    while x < 9:
        userInput = list(input("Give me coords, when 0,0 is top left corner and 2,2 is bottom right corner\n"))
        if "," in userInput:
            del userInput[userInput.index(",")]
        update(userInput, game, x)
        x += 1


def update(userInput, game, turn):
    if turn % 2:
        game[int(userInput[0])][int(userInput[1])] = "X"
    else:
        game[int(userInput[0])][int(userInput[1])] = "O"
    print(game)


if __name__ == '__main__':
    main()
