import scrapy
from ..items import TmdbdataItem


class tomato(scrapy.Spider):
    name = 'tmdb1'
    start_urls = [f'https://www.themoviedb.org/movie/top-rated?page={i}' for i in range(1, 50)]
    print('starturls' ,start_urls)
    def parse(self, response):
        items = TmdbdataItem()
        all_div_mov = response.css('.aligncenter')
        mainpage = response.css('#article_main_body .title::attr(href)').getall()
        print('mainpage-url', mainpage)
        for movies in mainpage:
            yield response.follow(movies, callback=self.parse_movie)

    def parse_movie(self, response):
        # Extract movie details
        title =response.css('.blurred ::attr(alt)').get()
        rating = response.css('.user_score_chart::attr(data-percent)').get()
        year = response.css('.release::text').re_first(r'\d{4}')
        genre = response.css('.genres a::text').getall()
        runtime = response.css('.runtime::text').get().strip()
        director = response.css('.profile:nth-child(1) a::text').get()
        image = response.css('.blurred ::attr(src)').get()


        yield {
            'Title': title,
            'Rating': rating.strip() if rating else 'N/A',
            'Year': year,
            'Genre': genre,
            'Runtime': runtime,
            'Director': director,
            'Image': image
        }

        # nextpage =  response.css('pagination_page_1 a::attr(href)').get()
        # print(nextpage)
        # if nextpage is not None:
        #     yield response.follow(nextpage, callback=self.parse)