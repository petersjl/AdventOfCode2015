from pathlib import Path
from time import perf_counter as timer

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = list(map(lambda s: int(s) ,path.open().read().split('\n')))
	return input

def main():
	containers = parseInput()
	liters = 150
	workingCombos = countContainerCombinations(containers, [], liters)
	print(f'There are {workingCombos} working combinations of containers')
	return

def countContainerCombinations(containers:list[int], chosen:list[int], total:int) -> int:
	if total < 0: return 0
	if total == 0: return 1
	if len(containers) == 0: return 0
	
	count = 0
	con = containers[0]
	newContainers = containers.copy()
	newContainers.remove(con)
	newChosen = chosen.copy()
	newChosen.append(con)

	count += countContainerCombinations(newContainers, newChosen, total - con)
	count += countContainerCombinations(newContainers, chosen, total)
	return count

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')