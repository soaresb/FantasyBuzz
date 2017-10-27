import nflgame
import requests
from lxml import html
import json
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
# games = nflgame.games(2013, week=1)
# players = nflgame.combine_game_stats(games)
# for p in players.rushing().sort('rushing_yds').limit(5):
#     msg = '%s %d carries for %d yards and %d TDs'
#     print msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds)
def main():
	new_player_dict={}
	for i in nflgame.players.items():
		if i[1].status == 'ACT' and i[1].position:
			if i[1].position == 'QB':
				headers = {'User-Agent': USER_AGENT}
				url=i[1].profile_url
				page = requests.get(url,headers=headers)
				tree = html.fromstring(page.content)
				pic_url = tree.xpath("//div[@class='player-photo']/img/@src")[0]
				
				new_player_dict[i[1].full_name] = [pic_url,i[1].position,i[1].team]
				print i[1].full_name, i[1].status, i[1].position
			elif i[1].position == 'RB':
				headers = {'User-Agent': USER_AGENT}
				url=i[1].profile_url
				page = requests.get(url,headers=headers)
				tree = html.fromstring(page.content)
				pic_url = tree.xpath("//div[@class='player-photo']/img/@src")[0]
				new_player_dict[i[1].full_name] = [pic_url, i[1].position,i[1].team]

			elif i[1].position == 'WR':
				headers = {'User-Agent': USER_AGENT}
				url=i[1].profile_url
				page = requests.get(url,headers=headers)
				tree = html.fromstring(page.content)
				pic_url = tree.xpath("//div[@class='player-photo']/img/@src")[0]
				new_player_dict[i[1].full_name] = [pic_url,i[1].position,i[1].team]

			elif i[1].position == 'TE':
				headers = {'User-Agent': USER_AGENT}
				url=i[1].profile_url
				page = requests.get(url,headers=headers)
				tree = html.fromstring(page.content)
				try:
					pic_url = tree.xpath("//div[@class='player-photo']/img/@src")[0]
				except:
					pass
				new_player_dict[i[1].full_name] = [pic_url,i[1].position,i[1].team]
		
	
	with open('datateams.json', 'w') as fp:
		json.dump(new_player_dict, fp) 

	return new_player_dict
if __name__ == '__main__':
	main()
