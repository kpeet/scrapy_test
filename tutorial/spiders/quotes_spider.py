import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes" # como vamos a indicar que spider correr

    def start_requests(self):

        #Paginas a scrapear
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',

        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2] # extrae el numero de la página desde url
        filename = 'quotes-%s.html' % page # archivo donde guardaré los datos scrapeados
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('SAVED file %s' % filename)