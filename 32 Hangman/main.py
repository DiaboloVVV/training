import random as r


def picking_word():
    lines = []
    with open('sowpods.txt', 'r') as f:
        lines = f.readlines()
    random_word = r.choice(lines)
    print("Welcome to Hangman!\n")
    return random_word

def main():
    random_word = list(picking_word())
    del random_word[len(random_word)-1]
    word_len = list("_" * len(random_word))
    x = 0
    somestring = ""
    for elem in random_word:
        somestring += elem
    while True:
        for elem in word_len:
            print(elem, end=" ")
        if "_" not in word_len:
            print(f"YOU GUESSED IT!")
            break
        user = input("\nGuess your letter: ").upper()
        if somestring == user:
            print(f"YOU GUESSED IT! THE WORD IS: {somestring}")
            break

        if user in random_word:
            print(f"There is: {user} {random_word.count(user)} times!")
            for elem in range(random_word.count(user)):
                word_len[random_word.index(user)] = user
                random_word[random_word.index(user)] = "1"
        else:
            print("Incorrect!")
            x += 1

        if x == 6:
            print(f"You lost! The word was {somestring}")
            break


if __name__ == '__main__':
    main()
