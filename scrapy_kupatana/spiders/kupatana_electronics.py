import scrapy
import re
from bs4 import BeautifulSoup
from resusables.api.apimodules import apimodules
from requests import Session


class kupatana_electronics(scrapy.Spider):
    name = "kupatana_electronics"

    start_urls = [
        #'https://kupatana.com/search/region,21/category,electronics/sPriceMin,492360/sPriceMax,186873000/currency,TZS/iPage,1',
        'https://kupatana.com/real-estate_buy-and-sell-dar-es-salaam-r21',
    ]

    def get_kupatana_phone_number(self, product_id, json=None):
        url = 'https://kupatana.com/oc-content/themes/dohi/api/item-phone-number.php'
        self.client = Session()
        self.client.verify = False
        self.client.headers.update({'Content-Type': 'application/json'})
        json = {"id": product_id}
        return self.client.post(url, json=json)

    def parse(self, response):
        for div in response.selector.xpath('//div[@class="content-wrapper"]'):
            prod_id = (div.xpath('div[1]/@class').re(r'list-item-show_number\s*(.*)'))[0]
            resp = self.get_kupatana_phone_number(prod_id)
            if resp.status_code is not 200:
                raise ValueError('Fetching kupartana phone number operation failed: {} \n {}'.format(resp.status_code, resp.json()))
            phone_number = resp.json()['data']['phoneNumber']
            #if len(phone_number.strip()) < 5:
            #    continue
            #else:
            #    if phone_number.strip().startswith('+255'):
            #        phone_number = phone_number.split('+255')[1]
            #    elif phone_number.strip().startswith('255'):
            #        phone_number = phone_number.split('255')[1]
            yield{
                'Category'				: 'Electronics',
                'Phone Number'			: phone_number ,
            }

        next_page = response.xpath('//div[@class="pagination-next"]/a/@href').extract_first()
        page_no = response.xpath('//div[@class="pagination-next"]/a/@href').re_first(r'dar-es-salaam-r21/(.*)')
        print(next_page)
        print(page_no)

        if page_no is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
