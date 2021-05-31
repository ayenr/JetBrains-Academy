import requests
import string
from bs4 import BeautifulSoup
import os


class Webscraper():

    def __init__(self, page_number, article_type):
        self.url = None
        self.response = None
        self.response_soup = None
        self.article_list = []
        self.page_number = page_number
        self.article_type = article_type


    def get_response(self):
        self.response = requests.get(f'{self.url}', headers={'Accept-Language': 'en-US,en;q=0.5'})
        self.response_soup = BeautifulSoup(self.response.content, 'html.parser')

    def type_verification(self, num):
        articles = self.response_soup.find_all('article')


        for article in articles:
            types = article.find("span", {"data-test": "article.type"}).text.strip('\n')

            if types == self.article_type:
                article_url = "https://www.nature.com" + article.find('a')['href']
                body = self.get_body(article_url)
                self.doc_creator(article, body, num)

            else:
                pass



    def doc_creator(self, titled, body_item, num):
        translator = str.maketrans(' ', '_', string.punctuation)
        title = titled.find('h3', {'itemprop': "name headline"}).text.strip('\n')
        title_ = title.translate(translator)

        with open(os.path.join(f'Page_{num}', f'{title_}.txt'), 'wb') as f:
            f.write(str.encode(body_item))
            f.close()
        self.article_list.append(f'{title_}.txt')


    def get_body(self, url):
        r_ = requests.get(f'{url}', headers={'Accept-Language': 'en-US,en;q=0.5'})
        body_soup = BeautifulSoup(r_.content, 'html.parser')

        try:

            return body_soup.find("div", {"class": "c-article-body u-clearfix"}).text.strip()

        except:
            return body_soup.find("div", {"class": "article-item__body"}).text.strip()


    def directory_creator(self, p_number):
        try:
            os.mkdir(f"Page_{p_number + 1}")
        except OSError:
            pass

    def main(self):
        for n in range(self.page_number):
            self.url = f"https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={n + 1}"
            self.directory_creator(n)
            self.get_response()
            self.type_verification(n+1)

        return 'Saved all articles'


test = Webscraper(int(input()), input()).main()


print(test)
