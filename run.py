import MarioExtravaganza
import sys

if __name__ == "__main__":
	print("Welcome to the Mario Extravaganza team generator!!")
	try:
		names = sys.argv[1]
		obj = MarioExtravaganza.MarioExtravaganza()
		builtLst = obj.listBuild(names)
		shuffled = obj.lineupBuild(builtLst)
		print(obj.displayTeams(shuffled))
	except Exception as e:
		print(e)
