import requests
from lxml import html
from collections import Counter

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'

def main():
	print "Getting RotoWorld_DFS"
	headers = {'User-Agent': USER_AGENT}
	urls={}
	url="http://www.rotoworld.com/dailyList?sport=nfl"
	page = requests.get(url,headers=headers)
	count=0
	players=Counter()


	tree = html.fromstring(page.content)
	items = tree.xpath("//h3/a/@href")
	for i in items[:15]:
		if '#panel-title' not in i:
			if 'https' in i:
				urls[i]=1
			else:
				urls["http://www.rotoworld.com"+str(i)]=1

	for key in urls:
		count+=1
		currurl=key
		npage = requests.get(currurl)
		ntree = html.fromstring(npage.content)
		nitems = ntree.xpath("//div[@id='artpart']")
		for i in nitems:
			playerLst = i.xpath(".//p/a/text()")
			for player in playerLst:
				if player in players:
						players[player.encode('ascii', 'ignore').decode('ascii')]+=1
				else:
						players[player.encode('ascii', 'ignore').decode('ascii')]=1
	print players 
	return players
if __name__ == '__main__':
	main()