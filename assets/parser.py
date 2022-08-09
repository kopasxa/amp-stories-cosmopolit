from os import mkdir
import os
import re
import time
from turtle import title
from urllib import request
import config
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from requests_html import HTMLSession
from assets.page_builder import PageBuilder

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

    def find_poster_path(self, page, title):
        soup = bs(page, 'html.parser')
        try:
            reg = re.compile('[^0-9\s^a-zA-Z]')
            title = reg.sub('', title)

            pathDir = f'stories/{"_".join(title.split(" ")).split(".")[0]}'
            path = f'stories/{"_".join(title.split(" ")).split(".")[0]}/img/poster.jpg'
            result = soup.find('div', {'class': 'content-lede-image'}).find('img')['src'].split("?")[0]

            if result in "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/legacy-fre-image-placeholder-1648561128.png":
                return None

            try:
                if result != None:
                    if not os.path.exists(pathDir):
                        mkdir(pathDir)
                        mkdir(pathDir + "/img")
            except Exception as e:
                pass
                #print(e)

            if not os.path.exists(path):
                request.urlretrieve(result, path)

            return path
        except Exception as e:
            #print(e)
            return None

    def find_stories(self, page, title):
        soup = bs(page, 'html.parser')
        stories = []
        try:
            container = soup.find('div', {'class': 'content-container'})
            print("\n\nstart")
            #print(container.prettify())
            #print("\n\n")

            for el in container.find_all('p'):
                if not len(el.text) > 0:
                    el.extract()

            for el in container.find_all('div'):
                if not len(el.text) > 0:
                    el.extract()

            #print(container.prettify())
            print(title + "\n")
            print(len(container.select('.article-body-content h2 ~ div.embed img.lazyimage')))
            print(len(container.select('.article-body-content hr + .body-h2, div.embed + .body-h2')))
            print("\n\nend")

        except Exception as e:
            print(e)
            return None

    def run_page_builder(self, pages):
        for url in pages:
            session = HTMLSession()
            res = session.get('https://www.cosmopolitan.com' + url)
            article_soup = bs(res.text, 'html.parser')
            content_header = article_soup.find('div', {'class': 'content-header-inner'})
            content_header_title = content_header.find('h1', {'class': 'content-hed'}).text
            content_header_description = content_header.find('div', {'class': 'content-dek'}).text
            content_poster = self.find_poster_path(res.text, content_header_title)
            stories = self.find_stories(res.text, content_header_title)
            #print(content_poster)

            build = PageBuilder()