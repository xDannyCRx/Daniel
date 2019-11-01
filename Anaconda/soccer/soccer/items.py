# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.tem import Item, Field

class PruebaItem(Item):
	# Primary fields
	platillo = Field()
	precio = Field()

class SoccerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


