from collections import Counter
import sys
import pymongo
import json
import config
from fantasyfootballers.get_fan_footballers import main as get_fan_footballers
from fantasypros.get_fanpros import main as get_fanpros
from rotoworld.get_rotoworld import main as get_rotoworld
from ffcalculator.get_ffcalculator import main as get_ffcalculator
from fantasylabs.get_fantasylabs import main as get_fantasylabs
from rotoballer.get_rotoballer import main as get_rotoballer
from athlonsports.get_athlon import main as get_athlon
from breakingfootball.get_breakingfootball import main as get_breaking
from get_player_ids.get_player_ids import main as get_player_ids

def main():
	with open('./get_player_ids/data.json') as json_data:
	    d = json.load(json_data)
	
	uri = config.uri
	client = pymongo.MongoClient(uri)
	db = client.get_default_database()
	players = db['players']

	player_dict = d

	# fantasypros = Counter()
	# fantasyfootballers = Counter()
	# rotoworld=Counter()
	# ffcalculator = Counter()
	# fantasylabs = Counter()
	# rotoballer = Counter()
	# athlonsports = Counter()
	# breakingfootball = Counter()

	# fantasyfootballers = get_fan_footballers()
	# fantasypros = get_fanpros()
	# rotoworld = get_rotoworld()
	# ffcalculator = get_ffcalculator()
	# fantasylabs = get_fantasylabs()
	# rotoballer = get_rotoballer()
	# athlonsports = get_athlon()
	# breakingfootball = get_breaking()

	# dict_to_insert = fantasypros+fantasyfootballers+rotoworld+ffcalculator+fantasylabs+rotoballer+athlonsports+breakingfootball
	# arr_to_insert=[]
	# for key, value in dict_to_insert.items():
	# 	if key in player_dict:
	# 		temp={}
	# 		temp['name']=key
	# 		temp['value']=value
	# 		temp['url']=player_dict[key][0]
	# 		temp['pos']=player_dict[key][1]
	# 		arr_to_insert.append(temp)

	# players.insert(arr_to_insert,check_keys=False)
	cursor=players.find({"pos":'RB'},sort=[("value",-1)]).limit(25)
	for player in cursor:
		print player
	# players.update_many({},{'$set': {'value':1}})


if __name__ == '__main__':
	main()