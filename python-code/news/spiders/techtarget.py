import scrapy
import json
import time

class TechTargetSpider(scrapy.Spider):
    name = 'TechTarget'
    allowed_domains = ['www.techtarget.com']
    start_urls = ['http://www.techtarget.com/news']
    page_number = 0 #Page number of site
    page_number_limit = 4 # Limit number of pages scraped
    tt_page_dict = {} # Dictionary to contain all scraped page names

    
    def parse(self, response):
        article_list = [] # List to contain title/link info
        
        #Scrape info from pages
        if self.page_number < self.page_number_limit:
            headline =  response.xpath("//h2/text()").get()
            articles = response.xpath("//div/article/div/header/h5/a")
            
            for article in articles:
                title = article.xpath(".//text()").get()

                link = article.xpath(".//@href").get()

                article_list.append({'title': title, 'link': link})
                yield {
                    'title': title,
                    'link': link
                }

        #Assign unique key for the page name
        try:
            timestamp = str(time.time())[:16].replace('.','')
            self.tt_page_dict[f"{timestamp}-{headline.upper()}"] = article_list
            self.page_number +=1

            next_page = response.xpath("//div[@id='archiveListing']/div/ul/li[position()=1]/a/@href").get()
            if next_page:
                yield response.follow(next_page, callback=self.parse)
        except:
                print('No Page Left')

        jsonString = json.dumps(self.tt_page_dict) # Store all data in json
        jsonFile = open("tt_data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()