import random as r


def main():
    a = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()-=_+{}[]\|;:<,>./?"
    b = []
    user = int(input("How long do you want your password?"))
    # for i in range(0, user):
    #     b.append(a[r.randint(0, len(a))])
    # print("".join(b))
    print(["".join(a[r.randint(0, len(a))] for i in range(0, user))])


if __name__ == "__main__":
    main()
