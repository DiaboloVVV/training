import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    request = requests.get(url)
    soup = BeautifulSoup(request.text)
    for article in soup.find(class_="article main-content"):
        a = article.text
    print(a.replace(".", ".\n").strip())

    return 0


if __name__ == '__main__':
    main()
