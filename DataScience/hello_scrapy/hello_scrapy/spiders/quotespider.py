import scrapy
from ..items import HelloScrapyItem


class QuotespiderSpider(scrapy.Spider):
    name = 'quotespider'
    start_urls = ['https://jobinja.ir/jobs?&filters%5Bjob_categories%5D%5B%5D=&filters%5Bkeywords%5D%5B0%5D=python&filters%5Blocations%5D%5B%5D=&preferred_before=1669970813&sort_by=relevance_desc']

    def parse(self, response):
        work_positions = response.css(
            'li.o-listView__item.o-listView__item--hasIndicator.c-jobListView__item.o-listView__item__application')
        for item in work_positions:
            title = item.css("h3 a::text").get().strip()
            link = item.css("h3 a::attr(href)").get()
            # if link:
            #     yield response.follow(link, callback=self.parser_safe_dakjheloi)
            date_req = item.css("h3 span::text").get().strip()
            company = item.css("ul li span::text")[0].extract().strip()
            city = item.css("ul li span::text")[1].extract().strip()
            shoghl_info = HelloScrapyItem(
                title=title, link=link, company=company, date_req=date_req, city=city)
            yield shoghl_info
        next_page = response.css("div.paginator li a::attr(href)")[-1].get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parser_safe_dakjheloi(self, response):
        yield response.css("title")
