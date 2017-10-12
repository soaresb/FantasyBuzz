import requests
from lxml import html
from collections import Counter

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'

def main():
	print "Getting The Fantasy Footballers"
	headers = {'User-Agent': USER_AGENT}
	urls={}
	url="https://www.thefantasyfootballers.com/"
	page = requests.get(url,headers=headers)

	players=Counter()


	tree = html.fromstring(page.content)
	items = tree.xpath("//ul[@class='newscodes-wrap']")

	for i in items:
		temp = i.xpath(".//a/@href")
		# urls.append(i.xpath(".//a/@href"))
		for i in temp:
			if i in urls:
				pass
			if 'articles' in i:
				urls[i]=i

	for key in urls:
		currurl=key
		npage = requests.get(currurl)
		ntree = html.fromstring(npage.content)
		nitems = ntree.xpath("//div[@class='entry-content content']/p")
		for i in nitems:
			playerLst = i.xpath(".//a/text()")
			for player in playerLst:
				if player in players:
						player=player.replace('.',' ')
						players[player.encode('ascii', 'ignore').decode('ascii')]+=1
				else:
						players[player.encode('ascii', 'ignore').decode('ascii')]=1
	
	return players


if __name__ == '__main__':
	main()
