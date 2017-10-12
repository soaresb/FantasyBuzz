import requests
from lxml import html
from collections import Counter

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'

def main():

	headers = {'User-Agent': USER_AGENT}
	urls={}
	#fantasy pros already lists all of the articles nicely on thier website so I can gather the links from there
	url="https://www.fantasypros.com/nfl/advice/gridiron-experts.php"
	page = requests.get(url,headers=headers)

	players=Counter()


	tree = html.fromstring(page.content)
	items = tree.xpath("//div[@class='pull-left nine columns']")[0]
	links = items.xpath(".//strong/a/@href")
	for link in links:
		urls[link]=1

	for key in urls:
		currurl=key
		npage = requests.get(currurl,headers=headers)
		ntree = html.fromstring(npage.content)
		nitems = ntree.xpath("//div[@class='entry-content herald-entry-content']")
		for i in nitems:
			if 'podcast' not in currurl:
				playerLst =  i.xpath("//strong/text()")
				for player in playerLst:
					if 'Power Ranking' not in player and 'ESPN' not in player and 'Yahoo' not in player:
						player=player.strip(',')
						if player in players:
							players[player.encode('ascii', 'ignore').decode('ascii')]+=1
						else:
							isThere = player.find('(')
							if isThere != -1:
								players[player[:isThere].encode('ascii', 'ignore').decode('ascii')]=1
							else:
								players[player.encode('ascii', 'ignore').decode('ascii')]=1
	print players
	return players

		


if __name__ == '__main__':
	main()