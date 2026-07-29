# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RottentomatoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    Title = scrapy.Field()
    Release_Date = scrapy.Field()
    Critics_Rating = scrapy.Field()
    Director = scrapy.Field()
    Genre = scrapy.Field()
    Runtime = scrapy.Field()
    Audience_Rating = scrapy.Field()
    Boxoffice = scrapy.Field()
    Rating = scrapy.Field()

