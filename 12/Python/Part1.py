from pathlib import Path
from time import perf_counter as timer
import json

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = path.open().read()
	return json.loads(input)

def main():
	input = parseInput()
	count = countThing(input)
	print(f'Total count: {count}')
	return

def countThing(thing):
	thingtype = type(thing)
		
	if thingtype is int: return thing
	elif thingtype is str: return 0
	elif thingtype is dict: return countDict(thing)
	elif thingtype is list: return countList(thing)
	else:
		print(f'found unknown type {type(thing)}')
		exit(1)

def countDict(input:dict) -> int:
	count = 0
	for x in input:
		count += countThing(input[x])
	return count

def countList(input:list) -> int:
	count = 0
	for n in input:
		count += countThing(n)
	return count

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')