import scrapy 
import json
from scrapy.http import Request 

class ArticlesSpider (scrapy.Spider):
    name = 'scrape_articles'
    allowed_domains = ['politico.com']
    start_urls = []
        
    with open("myspider.json") as f:
        data = json.load(f)
        for i in data:
            temp = i['Link']
            start_urls.append(str(temp))

def parse (self, response):
    wrappert = response.css('div.page-wrapper')
    yield{
        'Title': wrapper.css("h1::tex").get(),
        'Text': wrapper.css("p::text").getall()
    }
     
        
