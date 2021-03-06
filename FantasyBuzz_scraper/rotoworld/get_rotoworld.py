import requests
from lxml import html
from collections import Counter

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'

def main():
	print "Getting RotoWorld"
	headers = {'User-Agent': USER_AGENT}
	urls={}
	url="http://www.rotoworld.com/features/nfl"
	page = requests.get(url,headers=headers)
	count=0
	players=Counter()


	tree = html.fromstring(page.content)
	items = tree.xpath("//h1/a/@href")
	for item in items[:30]:
		if 'podcast' not in item:
			try:
				urls["http://www.rotoworld.com"+str(item)]=1
			except Exception as e:
				print e
			
	

	#waiver
	

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
	
	return players, count

if __name__ == '__main__':
	main()