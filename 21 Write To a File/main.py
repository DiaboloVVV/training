import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://www.niebezpiecznik.pl'
    fileName = str(input("Please insert filename without it's extension!\n"))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    with open(f'{fileName}.txt', 'a', encoding='utf8') as f:
        for i in soup.find_all(class_="post"):
            f.write(i.a.text.replace("\n", " ").strip())


if __name__ == '__main__':
    main()
