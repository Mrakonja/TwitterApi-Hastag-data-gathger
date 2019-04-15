
def get_tweets_sum(keyword, consumer_key, consumer_secret, token,token_secret, TwitterSearch, time, yesterday):
	try:
		tso = TwitterSearch.TwitterSearchOrder()
		tso.set_keywords([keyword])
		tso.set_result_type('recent')
		tso.set_count(100)
		tso.set_since(yesterday)
		ts = TwitterSearch.TwitterSearch(
			consumer_key = consumer_key,
			consumer_secret = consumer_secret,
			access_token = token,
			access_token_secret = token_secret,
		)
		
		result = ts.search_tweets_iterable(tso)
		i=0
	
		for tweet in result:
			i = i +1
	

	except TwitterSearch.TwitterSearchException as e:
		print("sleeping mode 15 minutes")
		time.sleep(900)
		tso = TwitterSearch.TwitterSearchOrder()
		tso.set_keywords([keyword])
		tso.set_result_type('recent')
		tso.set_count(100)
		tso.set_since(yesterday)
		ts = TwitterSearch.TwitterSearch(
			consumer_key = consumer_key,
			consumer_secret = consumer_secret,
			access_token = token,
			access_token_secret = token_secret,
		)
		i = 0
		print("limit reached. Sleeping.")
		
		result = ts.search_tweets_iterable(tso)
		i=0
	
		for tweet in result:
			i = i +1

	print(i)
	return i

