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
        for a in soup.find_all("a", href=True, string=True):
            if a["href"].startswith("http"):  # в выборке попадаются некоторые гугловские ссылки, пропускаем их
                continue
            print("\n" + a["href"])


news = "https://news.google.com/"
Scraper(news).scrape()
