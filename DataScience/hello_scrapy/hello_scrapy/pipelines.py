from itemadapter import ItemAdapter
import pandas as pd


class HelloScrapyPipeline:
    def process_item(self, item, spider):
        return item


class TestOrderPipline:
    def process_item(self, item, spider):
        print("###########################################", spider.name)
        return item
