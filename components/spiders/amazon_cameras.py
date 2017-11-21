import scrapy
import re

class amz_cameras(scrapy.Spider):
	name = "scrapy_amz_cameras"
	
	start_urls = [	
			'https://kupatana.com/search/region,21/category,electronics/sPriceMin,492360/sPriceMax,186873000/currency,TZS/iPage,1',
	]
	
	
	def parse(self, response):
		count = "3"
	
		for div in response.selector.xpath('//div[@class="s-item-container"]'):
			price_with_offer= div.xpath('div[@class="a-row a-spacing-mini"][2]/div[2]/span[2]/text()').re_first(r'\((.*)\)')
			if price_with_offer is not None:
				build_absolute_url = div.xpath('div[@class="a-row a-spacing-bases"]/div/div/a/@href').extract_first()
			#match=re.search(u'\((.*)\)',price_with_offer)
			#offer=match.group(1)
			
				yield{
					#'url'		: div_off.xpath('a/@href').extract_first(),
					'category_id'				: 'Electronics',
					'sub_category_id'			: 'Cameras',
					'website_id'				: 'amazon',
					'url_id'					: response.urljoin(build_absolute_url),
					'offer_description'			: div.xpath('div[@class="a-row a-spacing-mini"][1]/div[1]/a/h2/text()').extract_first(),
					'offer_description_1'		: '',	
					'offer_description_2'		: '',
					'offer_discount'			: price_with_offer,#offer.strip(' ')
					'offer_old_price'			: '',
					'offer_new_price'			: '',
					'best_deals'				: '',
					#'pdp_url'		: response.urljoin(build_absolute_url),
					#'short_desc' 	: div_off.xpath('a/div[@class="__description"]/h4/text()').extract_first(),
					#'detail_desc'	: div_off.xpath().extract_first(),
					#'expiry_date' 	: div_off.xpath('a/div[@class="__description"]/p/span/text()').extract_first(),
					#'img_url'		: div_off.xpath('a/div[@class="__img"]/img/@src').extract_first(),
				}
			
		next_page = response.xpath('//a[@id="pagnNextLink"]/@href').extract_first()
		page_no = response.xpath('//a[@id="pagnNextLink"]/@href').re_first(r'&page=(.*)&')
		print(next_page)
		print(page_no)
		
		if next_page is not None:
			if page_no <= count:
				next_page = response.urljoin(next_page)
				yield scrapy.Request(next_page, callback=self.parse)
