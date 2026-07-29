import scrapy
from ..items import RottentomatoItem
from scrapy import Request
import random
import re

class tomato(scrapy.Spider):

    name = 'tomatoo'
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
        all_div_mov = response.css('.aligncenter')
        mainpage = response.css('#article_main_body .title::attr(href)').getall()
        for movies in mainpage:
            yield response.follow(movies, callback=self.parse_movie)
            
        
    def parse_movie(self, response):
        items = RottentomatoItem()
        # Extract movie details
        items['Title'] = response.css('.unset span::text').get() 
        items['Critics_Rating'] = response.css('rt-button:nth-child(3) rt-text::text').get()
        items['Audience_Rating'] = response.css('rt-link~ rt-button rt-text::text').get()
        items['Director'] = response.css('.category-wrap:nth-child(1) rt-link::text').getall()
        genre=[]
        # release_Date = response.css('.unset+ rt-text::text').get()
        # items['Release_Date'] =  release_Date.split(' ',1)
        # items['Genre'] = response.css('.category-wrap:nth-child(7) rt-link::text').getall()
        for i in range(20):
            if response.css(f'rt-text:nth-child({i})::attr(slot)').get() == 'duration':
                runtime = response.css(f'rt-text:nth-child({i})::text').get()
                items['Runtime'] = runtime
            elif response.css(f'rt-text:nth-child({i})::attr(slot)').get() == 'genre':
                genre.append(response.css(f'rt-text:nth-child({i})::text').get())    
            # elif response.css(f'rt-text:nth-child({i})::attr(slot)').get() == 'releaseDate':
            #     releaseDate = response.css(f'rt-text:nth-child({i})::text').get()
            #     items['Release_Date'] = releaseDate.split(' ',1)[1]

        genre_list = ','.join(genre)
        print('list is',genre_list)
        items['Genre'] = genre_list

        rele = False
        bo = False
        rat = False
        prod = False
        for i in range(20):  
            if rele == False: 
                a = response.css(f'.category-wrap:nth-child({i}) rt-text::text').get()
                if a == "Release Date (Theaters)":
                    releaseDate = response.css(f'.category-wrap:nth-child({i}) dd rt-text::text').get()
                    print(f'release date is {releaseDate}')
                    if releaseDate is not None:
                        rdate = releaseDate.split(' ')[:-1]
                        items['Release_Date'] = ' '.join(rdate)
                        rele = True
                    else :
                        items['Release_Date'] = 'None'
            if bo == False: 
                b = response.css(f'.category-wrap:nth-child({i}) rt-text::text').get()
                if b == "Box Office (Gross USA)":
                    boxoffice = response.css(f'.category-wrap:nth-child({i}) dd rt-text::text').get()
                    if boxoffice is not None:
                        items['Boxoffice'] = boxoffice
                        bo = True
                    else :
                        items['Boxoffice'] = 'None'
                else:
                    items['Boxoffice'] = 'None'
            if rat == False: 
                r = response.css(f'.category-wrap:nth-child({i}) rt-text::text').get()
                if r == "Rating":
                    rating = response.css(f'.category-wrap:nth-child({i}) dd rt-text::text').get()
                    if rating is not None:
                        items['Rating'] = rating
                        rat = True
                    else :
                        items['Rating'] = 'None'
                else:
                    items['Rating'] = 'None'
        yield items
