def main():
    number = int(input())
    if number % 4 == 0:
        print(f"{number} is dividable by 4!")
    elif number % 2 == 0:
        print(f"{number} is even!")
    else:
        print(f"{number} is odd!")


if __name__ == "__main__":
     main()