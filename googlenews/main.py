import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        soup = BeautifulSoup(html, "html.parser")
        # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#the-string-argument
        for tag in soup.find_all("a", string=True):
            url = tag.get("href")
            if url is None:
                continue
            if url.startswith("http"):  # в выборке попадаются некоторые гугловские ссылки, пропускаем их
                continue
            print("\n" + url)


news = "https://news.google.com/"
Scraper(news).scrape()
