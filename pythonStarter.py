from pathlib import Path
from time import perf_counter as timer

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = path.open().read()
	return input

def main():
	input = parseInput()
	return

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')