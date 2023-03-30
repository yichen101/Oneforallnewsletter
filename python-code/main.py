#Import All Spiders
from news.spiders.financialtimes import FinancialTimesSpider
from news.spiders.telegraph import TelegraphSpider
from news.spiders.economist import EconomistSpider
from news.spiders.wallstreetjournal import WallStreetJournalSpider
from news.spiders.fool import FoolSpider
from news.spiders.techtarget import TechTargetSpider
from news.spiders.spectator import SpectatorSpider

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from uploadtofirebase import upload_to_firebase

def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(FinancialTimesSpider)
    process.crawl(TelegraphSpider)
    process.crawl(EconomistSpider)
    process.crawl(WallStreetJournalSpider)
    process.crawl(FoolSpider)
    process.crawl(TechTargetSpider)
    process.crawl(SpectatorSpider)
    process.start()

if __name__ == '__main__':
    main()
    upload_to_firebase()