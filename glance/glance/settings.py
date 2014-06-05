# Scrapy settings for glance project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'glance'

SPIDER_MODULES = ['glance.spiders']
NEWSPIDER_MODULE = 'glance.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'glance (+http://www.yourdomain.com)'
