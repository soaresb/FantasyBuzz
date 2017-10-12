import requests
from lxml import html
from collections import Counter

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'

def main():
	print "Getting FantastyLabs"
	headers = {'User-Agent': USER_AGENT}
	urls={}
	url="http://www.fantasylabs.com/articles/category/nfl/"
	page = requests.get(url,headers=headers)

	players=Counter()


	tree = html.fromstring(page.content)
	items = tree.xpath("//div[@class='col-sm-6 col-xs-12']/a/@href")
	for item in items:
		if item not in urls:
			urls[item]=1

	for key in urls:
		currurl=key
		npage = requests.get(currurl,headers=headers)
		ntree = html.fromstring(npage.content)
		nitems = ntree.xpath("//div[@class='post-content']/p/strong/text()")
		for name in nitems:
			player=name.encode('ascii', 'ignore').decode('ascii')
			if player in players:
				players[player]+=1
			else:
				players[player]=1
	
	return players

if __name__ == '__main__':
	main()