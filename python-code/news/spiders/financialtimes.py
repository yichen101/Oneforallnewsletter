import scrapy
import json
import time

class FinancialTimesSpider(scrapy.Spider):
    name = 'financialtimes'
    allowed_domains = ['www.ft.com']
    start_urls = ['http://www.ft.com']

    page_number = 1 #Page number of site
    ft_page_dict = {} # Dictionary to contain all scraped page names

    def parse(self, response):
        article_list = [] # List to contain title/link info
        current_page_name = response.xpath(f"//div[@class='o-header__container']/ul/li[position()={self.page_number}]/a/text()").get().replace('/','').upper()
        
        #Scrape info from pages
        if self.page_number != 1:
            articles = response.xpath("//div[@class='o-teaser__heading']/a")
            for article in articles:
                title = article.xpath(".//text()").get()

                link = article.xpath(".//@href").get()
                full_link = self.allowed_domains[0] + link

                article_list.append({'title': title, 'link': full_link})
                yield {
                    'title': title,
                    'link': full_link
                }
        else: #Run below for home page only
            articles = response.xpath("//div[contains(@class,'headline js-teaser-headline')]/a")
            for article in articles:
                title = article.xpath(".//span[contains(@class,'text')]/text()").get()

                link = article.xpath(".//@href").get()
                full_link = self.allowed_domains[0] + link

                article_list.append({'title': title, 'link': full_link})
                yield {
                    'title': title,
                    'link': full_link
                }

        #Assign unique key for the page name
        timestamp = str(time.time())[:16].replace('.','')
        self.ft_page_dict[f"{timestamp}-{current_page_name}"] = article_list
        self.page_number +=1

        #Scrape from other pages
        next_page = response.xpath(f"//div[@class='o-header__container']/ul/li[position()={self.page_number}]/a/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        else:
            print('No Page Left')

        jsonString = json.dumps(self.ft_page_dict) # Store all data in json
        jsonFile = open("ft_data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()