import scrapy
from scrapy import Request
import re
from ..items import TmdbdataItem
import random

class tmdbspider(scrapy.Spider):

    name = 'tmdb'
    # urls = []
    # for i in range(1, 50):
    #      urls.append([
    #         f'https://www.themoviedb.org/movie/top-rated?page={i}'
    #     ])
    # start_urls = urls
    start_urls = [f'https://www.themoviedb.org/movie/top-rated?page={i}' for i in range(1, 50)]

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
        "User-Agent": user_agent_list[random.randint(0, len(user_agent_list) - 1)],
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

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        print("Page URL : ", response.url)
        mainpage = response.css('.page_wrapper .card.style_1 .image .picture a::attr(href)').extract()
        for movies in mainpage:
            yield response.follow(movies, callback=self.parse_movie)
            break

    def parse_movie(self, response):
        # Extract movie details
        items = TmdbdataItem()
        #check titile
        items['title'] = response.css('.blurred ::attr(alt)').get()
        items['rating'] = response.css('.user_score_chart::attr(data-percent)').get()
        items['release_date'] = response.css('.release::text').re_first(r'\d{4}')
        items['genre'] = response.css('.genres a::text').getall()
        # if response.css('.runtime::text').get() is not None:
        items['runtime'] = response.css('.runtime::text').get().strip()
        # items['runtime'] = None
        items['director'] = response.css('.profile:nth-child(1) a::text').get()
        items['image_link'] = response.css('.blurred ::attr(src)').get()

        yield items

            #     title = movies.css('.24 a::text').extract()
        #     release_date = movies.css('p::text').extract()
        #     rating = all_div_mov('consensus tight outer_ring data-percent::numeric').extract()
        #     # mainpage = all_div_mov('a::attr(href)').get()
        #     # director =
        #
        #
        #     items['title'] = title
        #     items['release_date'] = release_date
        #     # items['rating'] = rating
        #     yield items
        #
        #
        # nextpage =  response.css('pagination_page_1 a::attr(href)').get()
        # print(nextpage)
        # if nextpage is not None:
        #     yield response.follow(nextpage, callback=self.parse)