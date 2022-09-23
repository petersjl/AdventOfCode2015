from pathlib import Path
from time import perf_counter as timer

minchar = ord('a')
maxchar = ord('z')
restricted = [ord('i'), ord('o'), ord('l')]

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = path.open().read()
	numlist = []
	for c in input:
		numlist.append(ord(c))
	return numlist

def main():
	input = parseInput()
	print(f'start input: {numsToString(input)}')
	while((not checkOne(input)) or (not checkTwo(input)) or (not checkThree(input))):
		increment(input)
	print(f'next password: {numsToString(input)}')
	return

def increment(l: list):
	i = len(l) - 1
	while i > 0:
		l[i] += 1
		if l[i] <= maxchar: return
		l[i] = minchar
		i -= 1

def checkOne(l:list) -> bool:
	for n in l:
		if n in restricted: return False
	return True

def checkTwo(l:list) -> bool:
	for i in range(len(l) - 2):
		if l[i + 1] == l[i] + 1:
			if l[i + 2] == l[i + 1] + 1: return True
	return False

def checkThree(l:list) -> bool:
	count = 0
	i = 0
	while i < len(l) - 1:
		if l[i] == l[i + 1]:
			count += 1
			if count == 2: return True
			i += 2
			continue
		i += 1
	return False

def numsToString(l:list) -> str:
	string = ""
	for n in l:
		string += chr(n)
	return string

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')