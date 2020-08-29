lineUpList = []

for races in range( 0, 3 ):
	for i in range( 0, 16 ):
		lineUp = '{0:04b}'.format(i)
		print lineUp
		if lineUp[0] == '0': team1 = 'Jay'
		if lineUp[0] == '1': team1 = 'Gabe'
		if lineUp[1] == '0': team2 = 'Vix'
		if lineUp[1] == '1': team2 = 'Jenna'
		if lineUp[2] == '0': team3 = 'Ian'
		if lineUp[2] == '1': team3 = 'Shaw'
		if lineUp[3] == '0': team4 = 'Damian'
		if lineUp[3] == '1': team4 = 'Will'
		lineUpString = "{}\t{}\t{}\t{}".format( team1, team2, team3, team4 )
		lineUpList.append( lineUpString )

import random
random.seed( 0 )

random.shuffle( lineUpList )

for row in lineUpList:
	print row





