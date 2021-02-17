def main():
    while True:
        play = input("Do you wanna play a game?\n")
        if play == "no":
            break
        elif play != "yes":
            print("Please answer yes/no")
        else:
            p1 = input("P1 choice: ")
            p2 = input("P2 choice: ")
            print('P1 wins' if p1 == "rock" and p2 == "scissors" else 'P1 wins' if p1 == "paper" and p2 == "rock" else 'P2 wins' if p2 == "rock" and p1 == "scissors" else 'P2 wins' if p2 == "paper" and p1 == "rock" else "Draw")


if __name__ == "__main__":
    main()
