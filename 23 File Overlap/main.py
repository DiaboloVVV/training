def main():
    prime_table = []
    with open('prime.txt', 'r') as f:
        line = f.readline()
        while line:
            line = line.strip()
            prime_table.append(line)
            line = f.readline()
    happy_table = []
    with open('happy.txt', 'r') as f:
        line = f.readline()
        while line:
            line = line.strip()
            happy_table.append(line)
            line = f.readline()
    print("Prime table: {} \nHappy table: {}".format(prime_table, happy_table))
    overlap_table = []
    for elem in happy_table:
        if elem in prime_table:
            overlap_table.append(elem)
            print(f"number {elem} overlaps")


if __name__ == '__main__':
    main()
