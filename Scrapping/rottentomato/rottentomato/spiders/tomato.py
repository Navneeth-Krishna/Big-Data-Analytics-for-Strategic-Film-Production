import scrapy
from ..items import RottentomatoItem
from scrapy import Request
import random

class tomato(scrapy.Spider):

    name = 'tomato'
    start_urls = [
        'https://editorial.rottentomatoes.com/guide/best-movies-of-all-time/'
    ]

    user_agent_list = [
    # Edge User Agents
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0',

    # Chrome User Agents
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',

    # Safari User Agents
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.1',

    # Firefox User Agents
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',

    # Opera User Agents
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.'
    ]

    headers = {
        "User-Agent": user_agent_list[random.randint(0, len(user_agent_list)-1)],
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }

    def parse(self, response):

        items = RottentomatoItem()
        all_div_mov = response.css('.aligncenter')
        mainpage = response.css('#article_main_body .title::attr(href)').getall()
        for movies in mainpage:
            yield response.follow(movies, callback=self.parse_movie)
            break
        
    def parse_movie(self, response):
        # Extract movie details
        title = response.css('.unset span::text').get() 
        rating = response.css('rt-button:nth-child(3) rt-text::text').get()
        year = response.css('.category-wrap:nth-child(9) dd rt-text::text').re_first(r'\d{4}')
        genre = response.css('.category-wrap:nth-child(7) rt-link::text').getall()
        runtime = response.css('rt-text:nth-child(6)::text').get()
        director = response.css('.category-wrap:nth-child(1) rt-link::text').get()

        yield {
            'Title': title,
            'Rating': rating.strip() if rating else 'N/A',
            'Year': year,
            'Genre': genre,
            'Runtime': runtime,
            'Director': director,
        }    


        # nextpage =  response.css('pagination_page_1 a::attr(href)').get()
        # print(nextpage)
        # if nextpage is not None:
        #     yield response.follow(nextpage, callback=self.parse)