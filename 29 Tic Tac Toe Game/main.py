import os


class TicTacToe():
    def __init__(self):
        self.game = [[" ", " ", " "],
                     [" ", " ", " "],
                     [" ", " ", " "]]
        self.start = 0

    def board(self):
        boardUpDown = " ---"
        for elem in range(3):
            boardleft = "   |"
            boardleft2 = "|"
            print(boardUpDown*3)
            print(boardleft2 + boardleft*3)
        print(boardUpDown*3)


    def boardUpdate(self):
        boardUpDown = " ---"
        print(boardUpDown * 3)
        for elem in range(3):
            # for element in range(3):
            print("| %s | %s | %s |" % (self.game[elem][0], self.game[elem][1], self.game[elem][
                    2]))
            print(boardUpDown * 3)


    def turnupdate(self, userInput, game, turn):
        if turn % 2:
            game[int(userInput[0])][int(userInput[1])] = "X"
            self.boardUpdate()
        else:
            game[int(userInput[0])][int(userInput[1])] = "O"
            self.boardUpdate()

    def checkingwincon(self):
        for x in range(9):
            try:
                self.userInput = list(input("Give me cords, when 0,0 is top left corner and 2,2 is bottom right corner\n"))

                if "," in self.userInput:
                    del self.userInput[self.userInput.index(",")]

                if self.game[int(self.userInput[0])][int(self.userInput[1])] == " ":
                    self.turnupdate(self.userInput, self.game, x)
                    x += 1
                else:
                    print('This place is taken! Please select diffrent one.')
                    self.checkingwincon()

                if x >= 5:
                    for elem in range(3):
                        for element in range(3):
                            try:
                                if self.game[elem][element] == self.game[elem + 1][element] and self.game[elem][element] == self.game[elem + 2][
                                    element]:
                                    print("Player {} has won!".format(self.game[elem][element]))
                                    exit
                            except IndexError:
                                continue
                    for i in range(3):
                        for j in range(3):
                            try:
                                if self.game[i][0] == self.game[i][j + 1] and self.game[i][j + 1] == self.game[i][j + 2]:
                                    print("Player {} has won".format(self.game[i][0]))
                                    exit
                            except IndexError:
                                continue

                    if self.game[self.start][self.start] == self.game[self.start + 1][self.start + 1] and self.game[self.start + 1][self.start + 1] == self.game[self.start + 2][
                        self.start + 2]:
                        print("Player {} has won!".format(self.game[self.start][self.start]))
                        exit()
                    elif self.game[self.start][self.start + 2] == self.game[self.start + 1][self.start + 1] and self.game[self.start + 1][self.start + 1] == \
                            self.game[self.start + 2][
                                self.start]:
                        print("Player {} has won!".format(self.game[self.start][self.start + 2]))
                        exit()
            except ValueError:
                print("Please insert correct coordinates")
                self.checkingwincon()
            except IndexError:
                print("Please insert correct coordinates")
                self.checkingwincon()
            except TypeError:
                print("Please insert correct coordinates")
                self.checkingwincon()


def main():
    tc = TicTacToe()
    tc.board()
    tc.checkingwincon()


if __name__ == '__main__':
    main()
