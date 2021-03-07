def main():
    game = [["O", "O", "X"],
            ["X", "O", "X"],
            ["O", "X", "X"]]
    for elem in range(3):
        for element in range(3):
            try:
                if game[elem][element] == game[elem+1][element] and game[elem][element] == game[elem+2][element]:
                    print("Player {} has won!".format(game[elem][element]))

            except IndexError:
                continue
    for i in range(3):
        for j in range(3):
            try:
                if game[i][0] == game[i][j+1] and game[i][j+1] == game[i][j+2]:
                    print("Player {} has won".format(game[i][0]))
            except IndexError:
                continue
    start = 0
    if game[start][start] == game[start+1][start+1] and game[start+1][start+1] == game[start+2][start+2]:
        print("Player {} has won!".format(game[start][start]))
    elif game[start][start+2] == game[start+1][start+1] and game[start+1][start+1] == game[start+2][start]:
        print("Player {} has won!".format(game[start][start+2]))
    return 0


if __name__ == '__main__':
    main()
