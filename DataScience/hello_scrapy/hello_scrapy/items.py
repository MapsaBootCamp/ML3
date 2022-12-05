# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HelloScrapyItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    date_req = scrapy.Field()
    company = scrapy.Field()
    city = scrapy.Field()
