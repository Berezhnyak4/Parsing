


from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from jobparser7 import settings
from jobparser7.spiders.leroymerlin import LeroymerlinSpider



if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeroymerlinSpider, search='жидкие+обои')


    process.start()