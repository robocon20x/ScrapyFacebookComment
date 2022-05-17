# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FbscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    page = scrapy.Field()
    post = scrapy.Field()
    cmt = scrapy.Field()
