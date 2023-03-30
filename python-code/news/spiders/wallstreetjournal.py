import scrapy
import json
import time

class WallStreetJournalSpider(scrapy.Spider):
    name = 'wallstreetjournal'
    allowed_domains = ['www.wsj.com']
    start_urls = ['http://www.wsj.com']

    page_number = 1 #Page number of site
    wsj_page_dict = {} # Dictionary to contain all scraped page names

    def parse(self, response):
        article_list = [] # List to contain title/link info
        print(response.xpath(f"//header/nav/ul/li[position()=1]/a/text()").get())
        print("PRINT")
        print(type(response.xpath(f"//header/nav/ul/li[position()={self.page_number}]/a/text()").get()))
        current_page_name = response.xpath(f"//header/nav/ul/li[position()={self.page_number}]/a/text()").get().replace('.','').upper()
        #Scrape info from pages
        main_article_title = response.xpath("//h2/a/span/text()").get() # Some featured articles use <h2> tag
        main_article_link = response.xpath("//h2/a/@href").get()
        yield {
            'title': main_article_title,
            'link': main_article_link
        }
        
        articles = response.xpath("//h3/a")
        for article in articles:
            title = article.xpath(".//span/text()").get()

            link = article.xpath(".//@href").get() #Already full link
            if title is not None: #Do not add null titles
                article_list.append({'title': title, 'link': link})
                yield {
                    'title': title,
                    'link': link
                }

        #Assign unique key for the page name
        timestamp = str(time.time())[:16].replace('.','')
        self.wsj_page_dict[f"{timestamp}-{current_page_name}"] = article_list
        self.page_number +=1

        #Scrape from other pages
        next_page = response.xpath(f"//header/nav/ul/li[position()={self.page_number}]/a/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        else:
            print('No Page Left')

        jsonString = json.dumps(self.wsj_page_dict) # Store all data in json
        jsonFile = open("wsj_data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()