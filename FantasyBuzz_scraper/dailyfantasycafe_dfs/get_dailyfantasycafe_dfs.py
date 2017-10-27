import requests
from lxml import html
from collections import Counter

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'

def main():
	print "Getting FFCalculator"
	headers = {'User-Agent': USER_AGENT}
	urls={}
	url="https://www.dailyfantasycafe.com/daily-fantasy-football"
	page = requests.get(url,headers=headers)
	count=0
	players=Counter()
	dfs=Counter()

	tree = html.fromstring(page.content)
	mainitem = tree.xpath("//*[@id='main-wrapper']/main/div/div/div[2]/a/@href")
	urls[mainitem[0]]=1

	otheritems = tree.xpath("//div[@class='article-box-item']/a/@href")

	for i in otheritems:
		if 'dashboard' not in i:
			urls[i]=1

	for key in urls:
		count+=1
		currurl=key
		npage = requests.get(currurl,headers=headers)
		ntree = html.fromstring(npage.content)
		nitems = ntree.xpath("//p/strong/text()")
		h3items = ntree.xpath("//h3/text()")
		
		for i in nitems:
			if i in dfs:
				dfs[i.encode('ascii', 'ignore').decode('ascii')]+=1
			else:
				dfs[i.encode('ascii', 'ignore').decode('ascii')]=1
		
		for i in h3items:
			dash = i.find('-')
			if dash != -1:
				name = i[:dash-1].encode('ascii', 'ignore').decode('ascii')
				if 'vs' not in name:
					if name in dfs:
						dfs[name]+=1
					else:
						dfs[name]=1

		 
		return dfs

		




if __name__ == '__main__':
	main()