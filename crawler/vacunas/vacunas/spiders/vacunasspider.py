import scrapy
from vacunas.items import VacunasItem

class VacunasSpider(scrapy.Spider):
    name = 'vacunas'
    start_urls = ['https://www.ccss.sa.cr/web/coronavirus/vacunacion']

    def parse(self, response):
        item_total_vacunas = response.css('.marco h2.counter::text').getall()[0]
        item_primera_dosis = response.css('.marco h2.counter::text').getall()[1]
        item_segunda_dosis = response.css('.marco h2.counter::text').getall()[2]
        item_fecha = response.css('.row.fuente span::text').getall()[1].split(' ')[1]
        vacunasItem = VacunasItem(total_vacunas = item_total_vacunas, primera_dosis = item_primera_dosis, segunda_dosis = item_segunda_dosis, fecha = item_fecha)
        yield vacunasItem