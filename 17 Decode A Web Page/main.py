import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://www.niebezpiecznik.pl'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for i in soup.find_all(class_="post"):
        print(i.a.text.replace("\n", " ").strip())


if __name__ == '__main__':
    main()


# import requests
# from bs4 import BeautifulSoup
#
# base_url = 'http://www.nytimes.com'
# r = requests.get(base_url)
# soup = BeautifulSoup(r.text)
#
# for story_heading in soup.find_all(class_="story-heading"):
#     if story_heading.a:
#         print(story_heading.a.text.replace("\n", " ").strip())
#     else:
#         print(story_heading.contents[0].strip())