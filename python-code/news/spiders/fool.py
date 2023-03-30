import scrapy
import json
import time

class FoolSpider(scrapy.Spider):
    name = 'fool'
    allowed_domains = ['www.fool.co.uk','www.fool.com']
    start_urls = ['http://www.fool.co.uk/recent-headlines']

    page_number = 0 #Page number of site
    my_interested_pages = ['http://www.fool.co.uk/recent-headlines',
                           'http://www.fool.com/investing-news']
                           
    fool_page_dict = {} # Dictionary to contain all scraped page names

    
    def parse(self, response):
        article_list = [] # List to contain title/link info

        #Scrape info from pages
        if self.page_number == 0:
            headline = response.xpath("//header/h1/text()").get()
            articles = response.xpath("//main[@id='primary']/section/section/main/a")
            
            for article in articles:
                title = article.xpath(".//article/h3/text()").get()

                link = article.xpath(".//@href").get()

                teaser = article.xpath(".//article/p[@class='teaser-content']/text()").get()

                article_list.append({'title': title, 'link': link, 'teaser': teaser})
                yield {
                    'title': title,
                    'link': link,
                    'teaser': teaser
                }
        elif self.page_number == 1:
            headline = "US " + response.xpath("//header/h1/text()").get()
            articles = response.xpath("//div[@class='flex py-12px text-gray-1100']")
            for article in articles:
                title = article.xpath(".//div/a/h5/text()").get()

                link = article.xpath(".//a/@href").get()
                full_link = self.my_interested_pages[self.page_number] + link

                teaser = article.xpath(".//div/a/div/text()").get()

                article_list.append({'title': title, 'link': full_link, 'teaser': teaser})
                yield {
                    'title': title,
                    'link': link,
                    'teaser': teaser
                }

        #Assign unique key for the page name
        timestamp = str(time.time())[:16].replace('.','')
        self.fool_page_dict[f"{timestamp}-{headline.upper()}"] = article_list
        self.page_number += 1
        try:
            next_page = self.my_interested_pages[self.page_number]
            if next_page:
                yield response.follow(next_page, callback=self.parse)
        except:
            print('No Page Left')

        jsonString = json.dumps(self.fool_page_dict) # Store all data in json
        jsonFile = open("fool_data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()