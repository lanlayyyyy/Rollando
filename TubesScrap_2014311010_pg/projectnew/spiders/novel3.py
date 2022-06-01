import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes3"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/novel-super-gene-optimization-fluid-id/chapter-1/',
            'https://www.worldnovel.online/novel-super-gene-optimization-fluid-id/chapter-2/',
            'https://www.worldnovel.online/novel-super-gene-optimization-fluid-id/chapter-3/',
            'https://www.worldnovel.online/novel-super-gene-optimization-fluid-id/chapter-4/',
            'https://www.worldnovel.online/novel-super-gene-optimization-fluid-id/chapter-5/',
            'https://www.worldnovel.online/novel-super-gene-optimization-fluid-id/chapter-6/',
            'https://www.worldnovel.online/novel-super-gene-optimization-fluid-id/chapter-7/',
            'https://www.worldnovel.online/novel-super-gene-optimization-fluid-id/chapter-8/',
            'https://www.worldnovel.online/novel-super-gene-optimization-fluid-id/chapter-9/',
            'https://www.worldnovel.online/novel-super-gene-optimization-fluid-id/chapter-10/',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        yield{
            'text3':response.css('#soop > p ::text').extract()
        }