# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ImgdlItem(Item):
    referrer = Field()
    # title = Field()
    image_urls = Field()
    images = Field()
    # date_created = Field()
