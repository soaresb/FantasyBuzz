import requests
from lxml import html
from collections import Counter

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'

def main():
	print "Getting RotoBaller"
	headers = {'User-Agent': USER_AGENT}
	urls={}
	#fantasy pros already lists all of the articles nicely on thier website so I can gather the links from there
	url="https://www.fantasypros.com/nfl/advice/rotoballer.php"
	page = requests.get(url,headers=headers)

	players=Counter()


	tree = html.fromstring(page.content)
	items = tree.xpath("//div[@class='pull-left nine columns']")[0]
	links = items.xpath(".//strong/a/@href")
	for link in links:
		urls[link]=1

	for key in urls:
		currurl=key
		if 'podcast' not in currurl:
			npage = requests.get(currurl,headers=headers)
			ntree = html.fromstring(npage.content)
			nitems = ntree.xpath("//a[@class='rbPlayer nfl']/text()")
			for i in nitems:
				if i in players:
					players[i.encode('ascii', 'ignore').decode('ascii')]+=1
				else:
					players[i.encode('ascii', 'ignore').decode('ascii')]=1

	return players
			

if __name__ == '__main__':
	main()