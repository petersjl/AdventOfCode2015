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
	strlen = 0
	for string in input:
		i = 1
		total += len(string)
		while i < len(string) - 1:
			strlen += 1
			if string[i] == "\\":
				i += 1
				if string[i] == "x":
					i += 2
			i += 1
	print(f'Physical count: {total}')
	print(f'Actual count:   {strlen}')
	print(f'Difference:     {total - strlen}')
	return

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')