import scrapy
import re
from scrapy import Spider as BaseSpider
from modules.gui import GUIMethods
from components.items import KupatanaItem


class KupatanaElectronics(BaseSpider):

    name = "kupatana-electronics"
    start_urls = [
    'https://kupatana.com/real-estate_buy-and-sell-kilimanjaro-r20',
    #'https://kupatana.com/real-estate_buy-and-sell-dar-es-salaam-r21',
    #'https://kupatana.com/real-estate_buy-and-sell-iringa-r7',
    #'https://kupatana.com/real-estate_buy-and-sell-arusha-r14',
    #'https://kupatana.com/real-estate_buy-and-sell-dodoma-r12',
    #'https://kupatana.com/real-estate_buy-and-sell-kigoma-r11',
]

    def __init__(self):
        super().__init__()

    def parse(self, response):
        for div in GUIMethods.get_product_div_tags(response):
            item = KupatanaItem()
            phone_number = GUIMethods.get_phone_number(div)
            next_page = GUIMethods.get_next_page_link(response)
            item['CATEGORY'] = 'Electronics'
            item['PHONENUMBER'] = phone_number
            item['HYPERLINK'] = next_page
            yield item

        next_page_1 = GUIMethods.get_next_page_link(response)
        page_no = GUIMethods.get_next_page_no(response)

        if page_no is not None:
            if page_no < 2:
                next_page_1 = response.urljoin(next_page_1)
                yield scrapy.Request(next_page_1, callback=self.parse)
