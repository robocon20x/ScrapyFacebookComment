from ntpath import join
import scrapy
from scrapy.http import FormRequest
from ..items import FbscrapyItem

class FbscrapingSpider(scrapy.Spider):
    name = 'fbscraping'
    cur_page = ''
    # page ='bichphuongofficial,tintucvtv24'
    # allowed_domains = ['www.facebook.com']
    start_urls = ['https://mbasic.facebook.com/login']

    def parse(self, response):
        token = response.css('form input::attr(value)').extract()
        lsd = token[0]
        jazoest = token[1]
        m_ts = token[2]
        li = token[3]
        try_number = token[4]
        unrecognized_tries = token[5]
        login = token[6]
        bi_xrwh = token[7]
        email = str(self.email)
        passw = str(self.passw)

        return FormRequest.from_response(response,formdata={
            'lsd' : lsd,
            'jazoest': jazoest,
            'm_ts':m_ts,
            'li': li,
            'try_number': try_number,
            'unrecognized_tries': unrecognized_tries,
             'email': email,
             'pass': passw,
             'login': login,
             'bi_xrwh': bi_xrwh
        },callback=self.start_scraping)

    def start_scraping(self,response):
        skip = response.css("div a::attr(href)").get()
        # if skip not None:
        # print(skip)
        if 'save-device' in str(skip):
            return response.follow(skip,callback=self.to_page)
    def to_page(self,response):
        temp = str(self.page).split(',')
        for i in temp:
            self.cur_page=i
   

            # yield scrapy.Request(f'https://touch.facebook.com/{i}',callback=self.get_story_list)
            yield scrapy.Request(f'https://touch.facebook.com/{i}',callback=self.get_story_list)

    def get_story_list(self,response):

        list_story = response.xpath('//a[contains(@data-click,"click_comment_ufi")]/@href')
        # print(list_story.extract())
        if len(list_story.extract()) ==0 :
            print('Khong the crawl duoc page nay')
        for i in list_story:
            # print(i)
            # break
            # print('#####################################')
            # # print(response.url)
            # print(i.extract())
            # print('#####################################')
            yield response.follow(f'https://touch.facebook.com{i.extract()}',callback=self.crawl_cmt)

    def crawl_cmt(self,response):

        item = FbscrapyItem()
        temp = response.xpath('//div[contains(@data-sigil,"comment-body")]')

        temp1 = response.xpath('//div[contains(@data-sigil,"comment-body")]//preceding-sibling::div/a')
        count = 1
        count1 = 1
        # temp2 = response.xpath('//div[contains(@data-ft,"*s")]/div/p//text()').extract()
        temp2 = response.xpath('//div[contains(@data-ft,"*s")]/div//text()').extract()
        temp2 = "".join(temp2) if temp2 else ""
        temp3 = response.xpath('//h3[contains(@data-gt,"C")]/span/strong/a/text()').extract_first()
        for i in temp:
            if not i:
                 continue
            test = i.xpath('text()').extract()
            test = "".join(test) if test else ""
            if 0 == len(test):
                continue
            # item['page'] = self.cur_page
            item['page'] = self.cur_page
            item['post'] = temp2
            item['cmt'] = test
            yield item
     



            
    