def main():
    userInput = int(input("How long Fibonacci would you like? \n"))
    fib = [1, 1]
    if userInput > 1:
        for elem in list(range(0, userInput-2)):
            fib.append(fib[elem] + fib[-1])
        print(fib)
    else:
        print([1])


if __name__ == "__main__":
    main()
