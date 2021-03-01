def main():
    basic_dict = {}
    with open('test.txt', 'r') as f:
        line = f.readline()
        while line:
            line = line.strip()
            if line in basic_dict:
                basic_dict[line] += 1
            else:
                basic_dict[line] = 1
            line = f.readline()
    print(basic_dict)


if __name__ == '__main__':
    main()
