# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


import scrapy
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from scrapy.pipelines.images import ImagesPipeline


class InstaparserPipeline:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.insta_friendship

    def process_item(self, item, spider):
        """Добавляем документ в коллекцию followers или following в зависимости от содержимого поля"""
        collection = self.mongobase[item['search_type']]
        # collection.drop()
        try:
            collection.update_one({'user_id': item['user_id']}, {'$set': item}, upsert=True)
        except DuplicateKeyError as e:
            print(e, item['user_id'])

        return item


class InstaImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photo']:
            try:
                yield scrapy.Request(item['photo'])
            except Exception as e:
                print(e)

    def file_path(self, request, response=None, info=None, *, item=None):
        """Создаем путь к аватаркам подписчиков и подписок вида:
        photos/id нашего основного пользователя/followers или following/id пользователя с аватарки.jpg
        В итоге получается папка для каждого пользователя-объекта скрапинга, в которой
        две подпапки для подписчиков и подписок
        """
        return f'{item["owner_id"]}/{item["search_type"]}/{item["user_id"]}.jpg'


