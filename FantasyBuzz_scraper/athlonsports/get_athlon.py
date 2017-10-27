import requests
from lxml import html
from collections import Counter

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'

def main():
	print "Getting Athlon Sports"
	headers = {'User-Agent': USER_AGENT}
	urls={}
	#fantasy pros already lists all of the articles nicely on thier website so I can gather the links from there
	url="https://www.fantasypros.com/nfl/advice/athlon-sports.php"
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
	# for i in urls:
	# 	if "waiver" in i:
	# 		print i
	# 	if "draftkings" in i:
	# 		print i
	
	
	for key in urls:
		count+=1
		currurl=key
		npage = requests.get(currurl,headers=headers)
		ntree = html.fromstring(npage.content)
		nitems = ntree.xpath("//h4/text()")
		for i in nitems:
			name = i.split(',')[0].encode('ascii', 'ignore').decode('ascii')
			isThere = name.find('(')
			if isThere != -1:
				name=name[:isThere-1]
			if 'START' not in name and 'MIGHT BE' not in name and 'SIT THESE' not in name and 'YOUVE' not in name and 'START' not in name and ' I ' not in name and 'You May Also Enjoy' not in name and 'Positional Rankings' not in name:
				if name in players:
					players[name]+=1
				else:
					players[name]=1
				# if 'draftkings' in currurl:
				# 	if name in dfs:
				# 		dfs[name]+=1
				# 	else:
				# 		dfs[name]=1
		
	return players, count


if __name__ == '__main__':
	main()