# import scrapy
# from ..items import PostscrapeItem

# class PostSpider(scrapy.Spider):
#     # name = "posts"

#     # # start_ulrs = ['http://blog.scrapinghub.com/page/1/','http://blog.scrapinghub.com/page/2/','https://vnexpress.net/gia-xang-co-the-tang-manh-4461438.html']
#     # start_ulrs = ['https://vnexpress.net/gia-xang-co-the-tang-manh-4461438.html']

#     # def parse(self,response):
#     #     # page = response.url.split('/')[-1]
#     #     # filename = f'posts-{page}.html'
#     #     filename = 'posts.html' 

#     #     with open(filename,'wb') as f:
#     #         f.write(response.body)

    
#     name = 'test'
#     start_urls = ['http://quotes.toscrape.com/']

#     def parse(self,response):
#         # title= response.css('title::text').extract()
#         # yield {'titletext-------------*****-------:': title} 
#         item = PostscrapeItem()
#         all_div_quotes = response.css('div.quote')
#         for quote in all_div_quotes:

#             title = quote.css('span.text::text').extract()
#             author = quote.css('.author::text').extract()
#             tag = quote.css('.tag::text').extract()

#             item['title'] = title
#             item['author'] = author
#             item['tag'] = tag


#             yield item
#             # yield {
#             #     'title': title,
#             #     'author': author,
#             #     'tag': tag
#             # }
#         next_page = response.css('li.next a::attr(href)').get()
#         if next_page is not None:
#             yield response.follow(next_page,callback = self.parse)