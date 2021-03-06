# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

# from itemadapter import ItemAdapter

import sqlite3

class BotPipeline:

	def __init__(self):
		
		self.con = sqlite3.connect("vikka_news.db")
		self.cur = self.con.cursor()
		self.create_table()
		
	def create_table(self):
		self.cur.execute("""CREATE TABLE IF NOT EXISTS news(
			id integer PRIMARY KEY AUTOINCREMENT,
			title TEXT,
			description TEXT,
			tags TEXT,
			url TEXT,
			news_date TEXT,
			UNIQUE(url)
			)""")

	def process_item(self, item, spider):

		self.cur.execute("INSERT OR IGNORE INTO news (title, description, tags, url, news_date) VALUES (?,?,?,?,?)", 
			(item["news_title"], item["news_description"], item["tags_string"], item["news_url"], item["news_date"]))
		self.con.commit()
		self.con.close()

		return item
