from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from jobparser8 import settings
from jobparser8.database_requests import get_data
from jobparser8.spiders.instagram import InstagramSpider



if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(InstagramSpider)
    process.start()
    get_data('2073401843')