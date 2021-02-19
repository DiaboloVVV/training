from datetime import date


def main():
    name = input("What's your name? \n")
    age = int(input("What's your age? \n"))
    print(f"Hello {name} in {100 - age + int(date.today().year)} you'll be 100 years old")
    return 0


if __name__ == '__main__':
    main()
