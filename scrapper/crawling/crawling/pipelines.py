# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class CrawlingPipeline:
    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'
        password = 'dharvi08' # your password
        database = 'quotes'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()
    def process_item(self, item, spider):
        self.cur.execute("insert into quote_content(title,content,url,datetime,image,author) values(%s,%s,%s,%s,%s,%s)",(item['title'],item['content'],item['url'],item['datetime'],item['image'],item['author']))
        self.connection.commit()
        return item
