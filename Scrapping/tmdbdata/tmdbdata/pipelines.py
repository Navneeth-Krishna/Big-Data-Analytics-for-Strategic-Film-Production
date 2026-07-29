# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline

# class TmdbdataPipeline:
#     def process_item(self, item, spider):
#         return item

class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # for image_url in item["img_links"]:
        #     print("URL1 : ", item)
        #     yield Request(image_url)
        if item["image_link"] != None:
            yield Request(item["image_link"])
        else:
            yield item

    def file_path(self, request, response=None, info=None, *, item=None):
        return "tmdbdata/imgs/" + f'{item["title"]}.jpg'