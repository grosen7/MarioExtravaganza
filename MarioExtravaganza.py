import random
from typing import List
from datetime import datetime

class MarioExtravaganza:
	def __init__(self):
		self.races = 0

	# Splits names into even numbers (if possible) and puts each into
	# there own list multiplied by the number of races. 
	# Returns 2d list of results 
	def listBuild(self, names: str, races: int) -> List[List[str]]:
		nameLst = names.replace(" ","").split(",")
		builtLst = list()
		self.races = races

		for i in range(0, len(nameLst), 2):
			team = nameLst[i: i+2]
			team *= races
			builtLst.append(team)
		
		return builtLst

	# Randomly shuffles each list in the 2d teams list parameter
	# Returns shuffled 2d list
	def listShuffle(self, teams: List[List[str]]) -> List[List[str]]:
		shuffled = list()

		for team in teams:
			random.shuffle(team)
			shuffled.append(team)

		return shuffled

	def displayTeams(self, teams: List[List[str]]) -> str:
		displayStr = ""

		for i in range(self.races):
			tmpStr = ""

			for j in range(len(teams)):
				tmpStr += "{}, ".format(teams[j][i])

			tmpStr = tmpStr[:-2]
			displayStr += "Race {}: {}\n".format(i+1, tmpStr)
			tmpStr = ""

		return displayStr

