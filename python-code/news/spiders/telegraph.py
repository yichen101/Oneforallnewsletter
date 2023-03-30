import scrapy
import json
import time

class TelegraphSpider(scrapy.Spider):
    name = 'telegraph'
    allowed_domains = ['www.telegraph.co.uk']
    start_urls = ['http://www.telegraph.co.uk']

    page_number = 0 #Page number of site
    telegraph_page_dict = {} # Dictionary to contain all scraped page names

    def parse(self, response):
        article_list = [] # List to contain title/link info
        articles = response.xpath("//h2[starts-with(@class,'list-headline')]/a")

        if self.page_number == 0:
            current_page_name = 'Home'
        elif 1 <= self.page_number < 8:
            current_page_name = response.xpath(f"//ul[contains(@class,'site-navigation__list--primary')]/li[position()={self.page_number}]/a/span/span/text()").get().replace('\n','').replace('\t','')

        #Scrape info from pages (limited to 8 pages)
        if self.page_number < 8:
            for article in articles:
                title = article.xpath(".//span/span/text()").get()

                link = article.xpath(".//@href").get()
                full_link = self.allowed_domains[0] + link
                
                article_list.append({'title': title, 'link': full_link})
                yield {
                    'title': title,
                    'link': full_link
                }

        #Assign unique key for the page name
        timestamp = str(time.time())[:16].replace('.','')
        self.telegraph_page_dict[f"{timestamp}-{current_page_name.upper()}"] = article_list
        print("COUNT:",self.page_number)
        self.page_number +=1
        
        #Scrape from other pages
        next_page = response.xpath(f"//ul[contains(@class,'site-navigation__list--primary')]//li[position()={self.page_number}]/a/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        else:
            print('No Page Left')
        jsonString = json.dumps(self.telegraph_page_dict)
        jsonFile = open("telegraph_data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()