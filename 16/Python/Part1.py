from pathlib import Path
import re
from time import perf_counter as timer

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = list(map(lambda s: re.split(": |, | ", s.strip()), path.open().read().split('\n')))
	aunts = {}
	for x in input:
		aunts[x[1]] = {}
		facts = x[2:]
		i = 0
		while i < len(facts):
			aunts[x[1]][facts[i]] = int(facts[i + 1])
			i += 2
	path = Path(__file__).parent / "../ticket.txt"
	input = list(map(lambda s: re.split(": |, | ", s.strip()), path.open().read().split('\n')))
	knowns = {}
	for x in input:
		knowns[x[0]] = int(x[1])
	return (aunts, knowns)

def main():
	(aunts, knowns) = parseInput()
	aunt = findAunt(aunts, knowns)
	if aunt == -1: print('Could not find aunt')
	else: print(f'Aunt Sue {aunt} gave the gift')

	return

def findAunt(aunts:dict[str,dict[str,int]], knowns:dict[str,int]) -> int:
	for aunt in aunts.keys():
		a = aunts[aunt]
		if checkAunt(a, knowns): return int(aunt)
	return -1

def checkAunt(aunt:dict[str,int], knowns:dict[str,int]) -> bool:
	for k in aunt.keys():
		if aunt[k] != knowns[k]: return False
	return True
		

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')