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
from gridironexperts.get_gridiron import main as get_gridiron
from rotoworld_dfs.get_rotoworld_dfs import main as get_rotoworld_dfs
from ffcalculator_dfs.get_ffcalculator_dfs import main as get_ffcalculator_dfs
from dailyfantasycafe_dfs.get_dailyfantasycafe_dfs import main as get_dailyfantasycafe_dfs

def main():
	with open('./get_player_ids/data.json') as json_data:
	    d = json.load(json_data)
	
	uri = config.uri
	client = pymongo.MongoClient(uri)
	db = client.get_default_database()
	players = db['players']
	dfs=db['dfs']

	player_dict = d

	fantasypros = Counter()
	fantasyfootballers = Counter()
	rotoworld=Counter()
	ffcalculator = Counter()
	fantasylabs = Counter()
	rotoballer = Counter()
	athlonsports = Counter()
	breakingfootball = Counter()


	fantasyfootballers, ffbcount = get_fan_footballers()
	fantasypros, fantasyproscount = get_fanpros()
	rotoworld, rotoworldcount = get_rotoworld()
	ffcalculator, ffcount, ffdfs = get_ffcalculator()
	fantasylabs, fantasylabscount = get_fantasylabs()
	rotoballer, rotoballercount = get_rotoballer()
	athlonsports, athloncount = get_athlon()
	breakingfootball, breakingcount, breakingfootballdfs = get_breaking()


	##
	##
	##DFS EXCLUSIVE
	##
	##
	gridironexpertsdfs = get_gridiron()
	rotoworld_dfs = get_rotoworld_dfs()
	ffcalculator_dfs = get_ffcalculator_dfs()
	dailyfantasycafe_dfs = get_dailyfantasycafe_dfs()

	dict_to_insert = fantasypros+fantasyfootballers+rotoworld+ffcalculator+fantasylabs+rotoballer+athlonsports+breakingfootball+gridironexpertsdfs+rotoworld_dfs+ffcalculator_dfs+dailyfantasycafe_dfs
	arr_to_insert=[]
	for key, value in dict_to_insert.items():
		if key in player_dict:
			temp={}
			temp['name']=key
			temp['value']=value
			temp['url']=player_dict[key][0]
			temp['pos']=player_dict[key][1]
			arr_to_insert.append(temp)

	players.insert(arr_to_insert,check_keys=False)
	# print ffbcount+fantasyproscount+rotoworldcount+ffcount+fantasylabscount+rotoballercount+athloncount+breakingcount
	# print gridironexpertsdfs+breakingfootballdfs+ffdfs+rotoworld_dfs+ffcalculator_dfs+dailyfantasycafe_dfs
	dfs_to_insert = gridironexpertsdfs+breakingfootballdfs+ffdfs+rotoworld_dfs+ffcalculator_dfs+dailyfantasycafe_dfs
	dfs_arr_to_insert=[]
	for key, value in dfs_to_insert.items():
		if key in player_dict:
			temp={}
			temp['name']=key
			temp['value']=value
			temp['url']=player_dict[key][0]
			temp['pos']=player_dict[key][1]
			dfs_arr_to_insert.append(temp)
	dfs.insert(dfs_arr_to_insert,check_keys=False)
	cursor=players.find({"pos":'RB'},sort=[("value",-1)]).limit(25)
	for player in cursor:
		print player
	players.update_many({},{'$set': {'value':1}})


if __name__ == '__main__':
	main()