from pathlib import Path
from time import perf_counter as timer

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = list(map(lambda s: int(s) ,path.open().read().split('\n')))
	return input

def main():
	containers = parseInput()
	liters = 150
	found = {}
	workingCombos = countContainerCombinations(containers, [], liters, found)
	minNum = min(found.keys())
	print(f'The smallest number of containers is {minNum} with {found[minNum]} combinations')
	return

def countContainerCombinations(containers:list[int], chosen:list[int], total:int, found:dict[int, int]) -> None:
	if total < 0: return
	if total == 0: 
		if found.get(len(chosen)): found[len(chosen)] += 1
		else: found[len(chosen)] = 1
		return
	if len(containers) == 0: return
	
	con = containers[0]
	newContainers = containers.copy()
	newContainers.remove(con)
	newChosen = chosen.copy()
	newChosen.append(con)
	countContainerCombinations(newContainers, newChosen, total - con, found)
	countContainerCombinations(newContainers, chosen, total, found)
	return

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')