import MarioExtravaganza
import sys

if __name__ == "__main__":
	print("Welcome to the Mario Extravaganza team generator!!")
	names = sys.argv[1]
	races = int(sys.argv[2])
	obj = MarioExtravaganza.MarioExtravaganza()
	builtLst = obj.listBuild(names, races)
	shuffled = obj.listShuffle(builtLst)
	print(obj.displayTeams(shuffled))
