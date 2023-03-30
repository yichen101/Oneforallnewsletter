import scrapy
import json
import time

class EconomistSpider(scrapy.Spider):
    name = 'economist'
    allowed_domains = ['www.economist.com']
    start_urls = ['http://economist.com']

    my_interested_pages = ['Home',
                            'The world this week',
                            'War in Ukraine',
                            'Recession watch',
                            'US politics',
                            'China',
                            'Britain',
                            'International',
                            'Business',
                            'Coronavirus',]
    page_number = 0 #Page number of site
    economist_page_dict = {} # Dictionary to contain all scraped page names
    menu_dict = {} # Dictionary to contain all pages items in menu
    run_once = True

    #Get all page names & links from the menu
    def get_pages(self, response):
        if self.run_once == True:
            pages = response.xpath("//li[starts-with(@class,'ds-navigation-list ds-navigation-list')]/ul/li/a/span")
            for page in pages:
                page_name = page.xpath(".//text()").get()
                page_link = page.xpath(".//parent::node()/@href").get()
                self.menu_dict[page_name] = page_link 
            self.run_once = False
        print(self.menu_dict.keys())

    def parse(self, response):
        article_list = [] # List to contain title/link info
        self.get_pages(response)
        
        #Scrape info from pages
        articles = response.xpath("//div[contains(@class,'e1mrg8dy0')]/div/h3/a")
        for article in articles:
            title = article.xpath(".//text()").get()

            link = article.xpath(".//@href").get()
            full_link = self.allowed_domains[0] + link

            article_list.append({'title': title, 'link': full_link})
            yield {
                'title': title,
                'link': full_link
            }

        #Assign unique key for the page name 
        timestamp = str(time.time())[:16].replace('.','')
        self.economist_page_dict[f"{timestamp}-{self.my_interested_pages[self.page_number].upper()}"] = article_list
        self.page_number += 1

        #Scrape from other pages
        try:
            print(self.my_interested_pages[self.page_number])
            if self.my_interested_pages[self.page_number] in self.menu_dict.keys():
                next_page = self.menu_dict[self.my_interested_pages[self.page_number]] # next page is link for the menu itme
                yield response.follow(next_page, callback=self.parse)
        except:
            print('No Page Left')
        
        jsonString = json.dumps(self.economist_page_dict) # Store all data in json
        jsonFile = open("economist_data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()