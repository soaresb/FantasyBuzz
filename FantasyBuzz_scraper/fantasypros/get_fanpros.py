import requests
from lxml import html
from collections import Counter

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'

def main():
	print "Getting Fantasy Pros"
	headers = {'User-Agent': USER_AGENT}
	urls={}
	url="https://www.fantasypros.com/nfl/articles/"
	page = requests.get(url,headers=headers)
	count=0
	players=Counter()


	tree = html.fromstring(page.content)
	items = tree.xpath("//div[@class='clearfix']")

	for item in items:
		url= item.xpath(".//span/a/@href")
		for i in url:
			if i:
				urls[i]=1
	#Waiver articles exost.  No dfs at the moment.  Streams also exist (can put into waivers)
	for key in urls:
		count+=1
		headers = {'User-Agent': USER_AGENT}
		url=key
		page = requests.get(url,headers=headers)
		tree = html.fromstring(page.content)
		items = tree.xpath('//*[@id="entry-content"]')
		for item in items:
			playerLst = item.xpath(".//a/text()")
			for player in playerLst:
				if player in players:
						players[player]+=1
				else:
					isThere = player.find('(')
					if isThere != -1:
						players[player[:isThere].encode('ascii', 'ignore').decode('ascii')]=1
					else:
						players[player.encode('ascii', 'ignore').decode('ascii')]=1
	
	return players, count


if __name__ == '__main__':
	main()