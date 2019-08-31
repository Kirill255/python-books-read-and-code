import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        soup = BeautifulSoup(html, "html.parser")
        base = "https://news.google.com/news"
        with open("output.txt", "w") as f:
            # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#the-string-argument
            for a in soup.find_all("a", href=True, string=True):
                if a["href"].startswith("http"):  # в выборке попадаются некоторые гугловские ссылки, пропускаем их
                    continue
                print("\n" + base + a["href"].lstrip("."))  # см. сноску внизу
                f.write(base + a["href"].lstrip(".") + "\n")


news = "https://news.google.com/"
Scraper(news).scrape()

"""
Google поменял структуру своего сайта news.google, теперь он не размещает прямые ссылки на новости, теперь мы
получаем ссылки такого вида "./articles/CAIiEDwxZBHnBE_hPHFkbmlEjSAqFwgEKg8IACoHCAowjuuKAzCWrzww14QY?hl=en-US&gl=US&ceid=US%3Aen",
тоесть начинающиеся с "./", при внутреннем переходе внутри сайта по такой ссылке, мы пападаем сначала на страницу
"https://news.google.com/news/articles/CAIiEDwxZBHnBE_hPHFkbmlEjSAqFwgEKg8IACoHCAowjuuKAzCWrzww14QY?hl=en-US&gl=US&ceid=US%3Aen",
тоесть начинающуюся с базового адреса "https://news.google.com/news" и уже затем редиректит на прямой источник новости,
поэтому мы у спарсенной ссылки удаляем символ "." из начала и + добавляем базовый адрес
Также попадаются рекламные ссылки самого Google и его сервисов и они в полном формате, тоесть с протоколом
например "https://www.google.com/intl/en/about/products", поэтому мы их просто пропускаем

https://docs.python.org/3/library/stdtypes.html#str.lstrip
https://docs.python.org/3/library/stdtypes.html#str.startswith
"""
