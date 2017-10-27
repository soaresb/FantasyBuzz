import requests
from lxml import html
from collections import Counter

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'

def main():
	print "Getting Breaking Football"
	headers = {'User-Agent': USER_AGENT}
	urls={}
	#fantasy pros already lists all of the articles nicely on thier website so I can gather the links from there
	url="https://www.fantasypros.com/nfl/advice/breaking-football.php"
	page = requests.get(url,headers=headers)
	count=0
	players=Counter()
	dfs=Counter()

	tree = html.fromstring(page.content)
	items = tree.xpath("//div[@class='pull-left nine columns']")[0]
	links = items.xpath(".//strong/a/@href")
	for link in links:
		if 'rankings' not in link:
			urls[link]=1
	#NO WAIVER WIRE ARTICLES FROM HERE.  THERE ARE DFS ARTICLES THOUGH
	for i in urls:
		if 'dfs' in i:
			print i
	 
	for key in urls:
		count+=1
		currurl=key
		npage = requests.get(currurl,headers=headers)
		ntree = html.fromstring(npage.content)
		nitems = ntree.xpath("//b/text()")
		strong = ntree.xpath("//strong/text()")
		if nitems:
			for i in nitems:
				isThere = i.find('vs')
				atThere = i.find('at')
				if isThere != -1:
					name = i[:isThere-1]
					if name in players:
						players[name.encode('ascii', 'ignore').decode('ascii')]+=1
					else:
						players[name.encode('ascii', 'ignore').decode('ascii')]=1
				
				elif atThere != -1:
					name=i[:atThere-1]
					if name in players:
						players[name.encode('ascii', 'ignore').decode('ascii')]+=1
					else:
						players[name.encode('ascii', 'ignore').decode('ascii')]=1
				else:
					if 'Sleeper' not in i and 'Starts' not in i and 'Sits' not in i and 'Drop' not in i and 'Saviors' not in i and 'Running Backs' not in i and 'Tight Ends' not in i and 'Wide Receivers' not in i and 'Quarterbacks' not in i:
						if i in players:

								players[i.encode('ascii', 'ignore').decode('ascii')]+=1
						else:
								players[i.encode('ascii', 'ignore').decode('ascii')]=1
		if strong:
			for i in strong:
				paren = i.find('(')
				if paren != -1:
					name=i[:paren-1]
					if name in players:
						players[name.encode('ascii', 'ignore').decode('ascii')]+=1
					else:
						players[name.encode('ascii', 'ignore').decode('ascii')]=1
					if 'dfs' in currurl:
						if name in dfs:
							dfs[name.encode('ascii', 'ignore').decode('ascii')]+=1
						else:
							dfs[name.encode('ascii', 'ignore').decode('ascii')]=1

				#print i
	
	return players, count, dfs
		

if __name__ == '__main__':
	main() 