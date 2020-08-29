import random
from typing import List, Dict
from datetime import datetime

class MarioExtravaganza:

	# Splits names into even numbers (if possible) and puts each 
	# team into a dictionary where the key is the player value
	# and the value is the player name. Appends dictionary to list
	def listBuild(self, names: str) -> List[dict]:
		nameLst = names.replace(" ","").split(",")

		if len(nameLst) == 8:
			dictLst = list()

			for i in range(0, len(nameLst), 2):
				team = nameLst[i: i+2]
				teamDict = {'0': team[0], '1': team[1]} 
				dictLst.append(teamDict)
		else:
			raise Exception("There must be eight players!!")
		
		return dictLst

	#uses binary values to assign players to a race
	# returns 2d list of strings with player lineup
	# for each race 
	def lineupBuild(self, teams: List[dict]) -> List[List[str]]:
		lineup = list()
		
		# loop through 16 binary variations
		for i in range(0,16):
			tmpLst = list()
			binList = list('{0:04b}'.format(i))

			# select player from each team based on binary value
			for j in range(0,4):
				player = teams[j][binList[j]]
				tmpLst.append(player)
			
			lineup.append(tmpLst)
		
		# multiply list by 3 and then shuffle
		lineup *= 3
		random.shuffle(lineup)
		return lineup

				
	# combines team list to string where each line is a race
	# and the lineup for the race
	def displayTeams(self, teams: List[List[str]]) -> str:
		displayStr = ""
		count = 0

		for team in teams:
			count += 1
			tmpStr = ", ".join(team)

			displayStr += "Race {}: {}\n".format(count, tmpStr)
			tmpStr = ""

		return displayStr