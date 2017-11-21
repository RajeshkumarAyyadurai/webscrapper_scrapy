from bases.selectors import Selectors
from modules.api.APIMethods import APIMethods

api = APIMethods()


def get_product_id(div):
    return (div.xpath(Selectors.KupatanaDict['DIV_GetClassName']).re(r'list-item-show_number\s*(.*)'))[0]


def get_product_div_tags(response):
    return response.selector.xpath(Selectors.KupatanaDict['DIV_ProductDescriptionBox'])


def get_next_page_link(response):
    return response.xpath('//div[@class="pagination-next"]/a/@href').extract_first()


def get_next_page_no(response):
    return response.xpath('//div[@class="pagination-next"]/a/@href').re_first(r'dar-es-salaam-r21/(.*)')


def get_phone_number(div):
    prod_id = get_product_id(div)
    return api.get_kupatana_phone_number(product_id=prod_id)


