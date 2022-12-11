import scrapy
from ..items import AmazonMLBookItem


class AmazonCrawlerSpider(scrapy.Spider):
    name = 'amazon_crawler'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/s?k=machine+learning+book&crid=W8WVMGJFVHOH&sprefix=machine+learning+book%2Caps%2C2980&ref=nb_sb_ss_ts-doa-p_1_21']

    def parse(self, response):
        amazon_machine_learning_books = response.xpath(
            "//div[@class='a-section a-spacing-small puis-padding-left-small puis-padding-right-small']")
        book_item = AmazonMLBookItem()
        for book in amazon_machine_learning_books:
            book_item['title'] = book.xpath('.//div/h2/a/span/text()').get()
            book_item['authors'] = book.xpath(
                './/a[@class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style"]/text()').getall()
            book_item['rate'] = book.xpath(
                './/span[@class="a-icon-alt"]/text()').get()
            yield book_item
