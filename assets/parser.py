import time
import config
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from requests_html import HTMLSession
from page_builder import PageBuilder

class Parse:
    def __init__(self):
        from selenium import webdriver

        self.search_url = config.initial_query_for_search
        self.options = webdriver.ChromeOptions()
        self.articles = []

        self.options.add_argument("--log-level=OFF")
        try:
            self.options.add_argument('--headless') # for firefox on server
        except:
            pass # for chrome of debug mode

        self.driver = webdriver.Chrome(options=self.options, executable_path="assets/chromedriver.exe")

    def search(self, filter):
        self.driver.get(url=self.search_url)
        

        wait = WebDriverWait(self.driver, 5)
        try:
            wait.until(lambda x: x.find_element(By.CSS_SELECTOR, "main.site-content"))
        except:
            raise Exception("Timeout error")

        self.driver.execute_script("window.scrollBy(0,250)")
        time.sleep(2)

        while True:
            try:
                if self.driver.find_element(By.CSS_SELECTOR, "button.load-more").get_attribute("style") == "display: block;":
                    self.driver.execute_script('document.querySelector("button.load-more").click();')
                else:
                    break
            except:
                break

        result = self.get_articles_by_filter(self.driver.page_source, filter)
        self.articles += result
        return result

    def get_articles_by_filter(self, page, filter):
        soup = bs(page, 'html.parser')
        arcticles_list = []
        articles = soup.find_all('div', {'class': 'simple-item'})

        for article in articles:
            if filter.lower() in str(article.find('div', {'class': 'simple-item-title'}).text).lower():
                session = HTMLSession()
                res = session.get('https://www.cosmopolitan.com' + article.find('a')['href'])
                article_soup = bs(res.text, 'html.parser')
                try:
                    try:
                        images = article_soup.find('div', {'class': 'listicle-body-content'}).find_all('img')
                    except:
                        images = article_soup.find('div', {'class': 'standard-body-content'}).find_all('img')
                except:
                    pass

                if len(images) > config.min_count_image_on_page:
                    if article.find('a')['href'] not in self.articles:
                        arcticles_list.append(article.find('a')['href'])

        return arcticles_list

    def find_poster_path(self, page):
        soup = bs(page, 'html.parser')
        try:
            return soup.find('div', {'class': 'article-hero-image'}).find('img')['src']
        except:
            return None

    def find_stories(self, page):
        soup = bs(page, 'html.parser')
        try:
            return soup.find('div', {'class': 'listicle-body-content'}).find_all('a')
        except:
            return None

    def run_page_builder(self, pages):
        for page in pages:
            build = PageBuilder()