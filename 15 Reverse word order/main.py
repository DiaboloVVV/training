def main():
    user = input("Insert long string\n").split()
    print(" ".join(user[::-1]))
    return 0


if __name__ == "__main__":
    main()
