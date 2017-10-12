import requests
from lxml import html
from collections import Counter

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'

def main():
	print "Getting FFCalculator"
	headers = {'User-Agent': USER_AGENT}
	urls={}
	url="https://fantasyfootballcalculator.com/articles"
	page = requests.get(url,headers=headers)

	players=Counter()


	tree = html.fromstring(page.content)
	items = tree.xpath("//div[@class='col-md-9']/a/@href")
	for item in items[:25]:
		urls["https://fantasyfootballcalculator.com"+item]=1
			

	for key in urls:
		currurl=key
		npage = requests.get(currurl,headers=headers)
		ntree = html.fromstring(npage.content)
		nitems = ntree.xpath("//li[@class='media list-group-item p-x-md p-t']/p/a/text()")
		for name in nitems:
			if 'Fantasy Football News' not in name and "Check out our latest FREE rankings!" not in name:

				if name in players:
					players[name.encode('ascii', 'ignore').decode('ascii')]+=1
				else:
					players[name.encode('ascii', 'ignore').decode('ascii')]=1
					
	return players



if __name__ == '__main__':
	main()