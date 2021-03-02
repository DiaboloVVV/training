def board(size):
    boardUpDown = " ---"
    boardleft = "|   "
    for elem in range(size):
        print(boardUpDown*size)
        print(boardleft*(size+1))
    print(boardUpDown*size)


def main():
    boardRendered = board(int(input("Please insert size of the board\n")))
    # print(boardRendered)
    return 0


if __name__ == '__main__':
    main()
