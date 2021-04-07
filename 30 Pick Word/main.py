import random as r


def main():
    lines = []
    with open('sowpods.txt', 'r') as f:
        lines = f.readlines()
    # random_word = r.choice(lines)
    print(r.choice(lines))
    return 0


if __name__ == '__main__':
    main()