def main():
    word = "don't nod"
    word = word.replace(' ', '')
    word = word.replace("'", "")
    checking = word[::-1]
    if checking == word:
        print("yay")


if __name__ == "__main__":
    main()
