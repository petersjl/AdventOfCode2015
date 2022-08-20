from os import access
from pathlib import Path
from time import perf_counter as timer

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = path.open().read().split("\n")
	return input

def main():
	input = parseInput()
	total = 0
	encoded = 0
	for string in input:
		i = 0
		total += len(string)
		encoded += 2
		for c in string:
			encoded += 1
			if c == "\\" or c == "\"":
				encoded += 1
			i += 1
	print(f'Physical count: {total}')
	print(f'Encoded count:   {encoded}')
	print(f'Difference:     {encoded - total}')
	return

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')