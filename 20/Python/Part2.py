from pathlib import Path
from time import perf_counter as timer

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = path.open().read()
	return int(input)

def main():
	targetPresents = parseInput()
	house = findHouse(targetPresents)
	print(f'The first house to get more than {targetPresents} present is {house}')
	return

def findHouse(presents:int) -> int:
	upperBound = calculateUpperBound(presents)
	houses = [address * 11 for address in range(upperBound + 1)]
	candidates = set()
	for elf in range(2, len(houses)):
		bound = min(upperBound, elf * 50)
		for address in range(elf * 2, bound + 1, elf):
			houses[address] += 11 * elf
			if houses[address] >= presents:
				candidates.add(address)
	return min(candidates)

def calculateUpperBound(presents:int) -> int:
	i = 0
	count = 0
	house = presents / 10
	while count < presents:
		i += 1
		if house % i == 0: count += i * 10
	return i

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')