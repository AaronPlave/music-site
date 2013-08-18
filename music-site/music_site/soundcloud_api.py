import soundcloud

def SC_Embed(url_lst):
	client = soundcloud.Client(client_id="858c98ac9ee828617aa6a2364d5b0b0a")
	embed_dict = {}
	bad = []
	for link in url_lst:
		try:
			# track_url = client.get('/resolve',url=link)
			embed_info = client.get('/oembed',url=link)
			embed_dict[link] = embed_info.html
		except Exception, e:
			print e
			bad.append(link)
			return (False,bad)
	return (True,embed_dict)
