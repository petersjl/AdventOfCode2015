from math import prod
from pathlib import Path
from re import T
from time import perf_counter as timer

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = list(map(lambda x: int(x), path.open().read().split('\n')))
	return input

def main():
	input = parseInput()
	input.reverse()
	collections = []
	allow = int(sum(input) / 3)
	findAllowedSets(allow, collections, input)
	collections.sort(key=lambda x: len(x))
	lowest = findLowestSet(collections, allow, input)
	print(lowest)
	return

# find (max) number of sets that have the correct sum of weights
def findAllowedSets(allowance:int, collection:list[list[int]], open:list[int], c:list[int] = [], sumc:int = 0, max:int = 1000) -> None:
	if sumc > allowance: return None
	if sumc < allowance:
		for i in range(len(open)):
			n = open[i]
			no = open.copy()
			no.pop(i)
			nc = c.copy()
			nc.append(n)
			nsum = sumc + n
			if nsum + sum(open[i:]) >= allowance:
				findAllowedSets(allowance, collection, no, nc, nsum)
			if len(collection) == max: return
		return None
	else:
		collection.append(c)

# find the lowest set based on number of items and then quantum entanglement
def findLowestSet(sets:list[list[int]], allowance:int, input:list[int]) -> tuple[int,int]:
	lowest = (1000, 10**9)
	for set in sets:
		if len(set) < lowest[0]: lowest = (len(set), prod(set))
		elif len(set) == lowest[0]:
			qe = prod(set)
			if qe < lowest[1]: lowest = (len(set), qe)
	return lowest

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')