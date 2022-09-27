from pathlib import Path
from threading import local
from time import perf_counter as timer

guestIds = {}

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = list(map(lambda s: s.split(" "), path.open().read().split('\n')))
	arrangements = {}
	for x in input:
		if not arrangements.get(x[0]):
			arrangements[x[0]] = {}
		arrangements[x[0]][x[10][:-1]] = int(x[3]) * (1 if x[2] == "gain" else -1) 

	return arrangements

def main():
	arrangements = parseInput()
	guests = list(arrangements.keys())
	print(guests)
	
	(happiness, bestList) = calculateHappiness(guests, [], arrangements)

	print(f'Best happiness is {happiness} in the arragement\n{bestList}')
	return

def calculateHappiness(toSeat:list, seated:list, arrangements:dict) -> tuple[int, list]:
	# if everyone is seated, calculate happiness
	if len(toSeat) == 0: return (calculateArrangementHappiness(arrangements, seated), seated)

	# add each remaining person to the list
	localMax = -10**9
	bestSeat = []
	for person in toSeat:
		newToSeat = toSeat.copy()
		newSeated = seated.copy()

		newToSeat.remove(person)
		newSeated.append(person)

		# if the new seated list is the best, return it
		(instanceMax, localSeated) = calculateHappiness(newToSeat, newSeated, arrangements)
		if instanceMax > localMax:
			localMax = instanceMax
			bestSeat = localSeated
	return (localMax, bestSeat)

def calculateArrangementHappiness(arrangements:dict, seats:list) -> int:
	count = 0
	for i in range(len(seats)):
		count += arrangements[seats[i]][seats[(i + 1) % len(seats)]]
		count += arrangements[seats[i]][seats[i - 1]]
	return count

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')