import scrapy
from ..items import PostscrapeItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
class PostSpider(scrapy.Spider):
    
    name = 'test'
    start_urls = ['https://quotes.toscrape.com/login']

    def parse(self,response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response,formdata={
            'csrf_token': token,
            'username': '123',
            'password': '123'
        },callback=self.start_scraping)
    def start_scraping(self,response):
         # title= response.css('title::text').extract()
        # yield {'titletext-------------*****-------:': title} 
        open_in_browser(response)
        item = PostscrapeItem()
        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:

            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            item['title'] = title
            item['author'] = author
            item['tag'] = tag


            yield item
            # yield {
            #     'title': title,
            #     'author': author,
            #     'tag': tag
        #     # }
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page,callback = self.parse)