# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VacunasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    total_vacunas = scrapy.Field()
    primera_dosis = scrapy.Field()
    segunda_dosis = scrapy.Field()
    fecha = scrapy.Field()
