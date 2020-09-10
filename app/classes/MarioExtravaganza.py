import random, math, requests, io, csv
from typing import List, Dict, IO
from datetime import datetime

class MarioExtravaganza:

	# Splits names into even numbers (if possible) and puts each 
	# team into a dictionary where the key is the player value
	# and the value is the player name. Appends dictionary to list
	def listBuild(self, names: str) -> List[dict]:
		nameLst = names.replace(" ","").split(",")
		teamCt = len(nameLst) / 2

		# validate that the team count is a factor of 48, 
		# greater than 0 and is an integer
		# throw exception if it isn't
		if teamCt.is_integer() and teamCt > 0 and 48 % teamCt == 0:
			dictLst = list()

			for i in range(0, len(nameLst), 2):
				team = nameLst[i: i+2]
				teamDict = {'0': team[0], '1': team[1]} 
				dictLst.append(teamDict)
		else:
			raise Exception("The number of teams must be a factor of 48!!")
		
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

				
	# writes each race lineup as a csv row to stringio
	# stringio data is returned to be downloaded by client
	def fileDataBuild(self, teams: List[List[str]]) -> IO[str]:
		# build stringio object and set csv writer
		# to write to stringio object
		data = io.StringIO()
		writer = csv.writer(data)
		count = 0

		# loop through each line in teams list
		for team in teams:
			count += 1

			# create row list, first index is race number
			# proceeding indexes are team lineups
			row = ["Race {}".format(count)]
			row.extend(team)

			# write row to stringio, then move byte offset to 
			# beginning of memory stream
			writer.writerow(row)
			yield data.getvalue()
			data.seek(0)
			data.truncate(0)
		
		return data

	# runs all methods to gather data from user, process data
	# and return final data to be downloaded as file.
	def process(self, request: requests) -> IO[str]:
		# create empty StringIO object
		fileData = io.StringIO()
		players = request.form["players"]
		builtLst = self.listBuild(players)
		shuffledTeams = self.lineupBuild(builtLst)
		fileData = self.fileDataBuild(shuffledTeams)
		return fileData