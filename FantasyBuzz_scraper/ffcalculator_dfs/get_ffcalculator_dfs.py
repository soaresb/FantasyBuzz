import requests
from lxml import html
from collections import Counter

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'

def main():
	print "Getting FFCalculator_DFS"
	headers = {'User-Agent': USER_AGENT}
	urls={}
	url="https://fantasyfootballcalculator.com/dfs"
	page = requests.get(url,headers=headers)
	count=0
	players=Counter()
	dfs=Counter()

	tree = html.fromstring(page.content)
	items = tree.xpath("//div[@class='col-md-9']/a/@href")
	for item in items[:2]:
		urls["https://fantasyfootballcalculator.com"+item]=1
	#/dfs for the dfs articles waivers for the waiver articles
	for key in urls:
		count+=1
		currurl=key
		npage = requests.get(currurl,headers=headers)
		ntree = html.fromstring(npage.content)
		nitems = ntree.xpath("//h3/strong/text()")
		for i in nitems:
			vs = i.find('vs')
			if vs != -1:
				name = i[:vs-1].encode('ascii', 'ignore').decode('ascii')
				if name in dfs:
					dfs[name]+=1
				else:
					dfs[name]=1
			paren = i.find('(')
			if paren != -1:
				name = i[:paren-1].encode('ascii', 'ignore').decode('ascii')
				if name in dfs:
					dfs[name]+=1
				else:
					dfs[name]=1
	return dfs



if __name__ == '__main__':
	main()