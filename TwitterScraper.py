from wordpress_xmlrpc import Client, WordPressPost, WordPressPage
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import posts
from datetime import date, timedelta
from dominate.tags import *
from Functions import *
import TwitterSearch
import dominate
import csv
import time
import datetime


global TwitterSearch, time

token  = #
token_secret = #
consumer_key  = #
consumer_secret = #


username = #
password = #
yesterday = date.today() - timedelta(days=2)

while True:
	f_reader = open("hastags.csv", "r")
	list_results = []
	data_reader = csv.reader(f_reader)
	for row in data_reader:
		result_name = get_tweets_sum(row[2], consumer_key, consumer_secret, token,token_secret, TwitterSearch, time, yesterday)
		result_dollar_name =  get_tweets_sum(row[3], consumer_key, consumer_secret, token,token_secret, TwitterSearch, time, yesterday)
		result_hash_name = get_tweets_sum(row[4], consumer_key, consumer_secret, token,token_secret, TwitterSearch, time, yesterday)
		result_at_name_official = get_tweets_sum(row[5], consumer_key, consumer_secret, token,token_secret, TwitterSearch, time, yesterday)
		result_at_full_name = get_tweets_sum(row[7], consumer_key, consumer_secret, token,token_secret, TwitterSearch, time, yesterday)
		try:	
				total = result_name + result_dollar_name + result_hash_name + result_at_name_official
		except:
			total = 0
		list_results.append([row[0], row[1], result_name,
							result_dollar_name, result_hash_name,
							result_at_name_official,
							result_at_full_name, total
							  ])
	
	
	list_results.sort(key=lambda x: x[-1], reverse=True)
	h = table()
	theader = tr()
	theader.add(th('Rank'))
	theader.add(th('Coin Name'))
	theader.add(th('Coin Ticker'))
	theader.add(th('$text'))
	theader.add(th('#tag'))
	theader.add(th('@mention'))
	theader.add(th('@mention'))
	theader.add(th('Total'))
	h.add(theader)
	i = 0
	for row in list_results[:101]:
		l = tr()
		i=i+1
		l.add(td(i))
		l.add(td(row[1]))
		l.add(td(row[2]))
		l.add(td(row[3]))
		l.add(td(row[4]))
		l.add(td(row[5]))
		l.add(td(row[6]))
		l.add(td(row[7]))
		h.add(l)
	now_date = datetime.datetime.utcnow()
	last_week = now_date - datetime.timedelta(days=7)
	today  = str(now_date.month) + "-" + str(now_date.day) + "-" +  str(now_date.year)
	week_ago = str(last_week.month) + "-" + str(last_week.day) + "-" +  str(last_week.year)
	wpai = #
	wp = Client(wpapi, username, password)
	css - #
	new_page = WordPressPost()
	new_page.title =  "from" + str(week_ago) +"to" + str(today)
	table_ = str(h)
    content = #
	new_page.content = content
	upload_page = WordPressPage()
	page_id = #
	upload_page.title = #
	upload_page.content =  str(css) + str(content)
	wp.call(posts.EditPost(page_id, upload_page))
	wp.call(posts.NewPost(new_page))
