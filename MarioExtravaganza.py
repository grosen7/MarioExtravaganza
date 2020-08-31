import random, math
from typing import List, Dict
from datetime import datetime

class MarioExtravaganza:

	# Splits names into even numbers (if possible) and puts each 
	# team into a dictionary where the key is the player value
	# and the value is the player name. Appends dictionary to list
	def listBuild(self, names: str) -> List[dict]:
		nameLst = names.replace(" ","").split(",")
		teamCt = len(nameLst) / 2

		# validate that the team count is a multiple of 48
		# throw exception if it isn't
		if teamCt > 0 and 48 % teamCt == 0:
			dictLst = list()

			for i in range(0, len(nameLst), 2):
				team = nameLst[i: i+2]
				teamDict = {'0': team[0], '1': team[1]} 
				dictLst.append(teamDict)
		else:
			raise Exception("The number of teams must be a multiple of 48!!")
		
		return dictLst

	# generates every combination of races lineups
	# these lineups are then mutliplied by a certain factor
	# so that there are 48 total races, then races are shuffled
	def lineupBuild(self, teams: List[dict]) -> List[List[str]]:
		lineup = list()
		teamLen = len(teams)
		combos = int(math.pow(2, teamLen))

		# loop through all different number of comboes
		for i in range(0, combos):
			tmpLst = list()
			# create list of binary values to represent 
			# current combinary
			binList = list('{:0{}b}'.format(i, teamLen))

			# select player from each team based on binary value
			for j in range(0, teamLen):
				player = teams[j][binList[j]]
				tmpLst.append(player)
			
			lineup.append(tmpLst)
		
		# multiply list by factor needed to make 48 races
		# then shuffle races
		factor = 48 // len(lineup)
		lineup *= factor
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