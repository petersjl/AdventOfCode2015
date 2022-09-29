from pathlib import Path
from time import perf_counter as timer

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = path.open().read().split("\n")
	i = 0
	conversions = dict[str, list[str]]
	conversions = dict()
	while input[i] != "":
		line = input[i].split(" => ")
		if conversions.get(line[0]) == None: conversions[line[0]] = []
		conversions[line[0]].append(line[1])
		i += 1
	molecule = input[i + 1]
	i = len(molecule) - 1
	parts = []
	while i > -1:
		if molecule[i].islower():
			parts.append(molecule[i-1:i+1])
			i -= 1
		else:
			parts.append(molecule[i])
		i -= 1
	parts.reverse()
	return (conversions, parts)

def main():
	(conversions, parts) = parseInput()
	count = countVariations(conversions, parts)
	print(f'There are {count} unique variations')
	return

def countVariations(conversions:dict[str, list[str]], parts:list[str]) -> int:
	variations = set()
	for i in range(len(parts)):
		part = parts[i]
		print(part)
		if conversions.get(part) == None: continue
		for replacement in conversions[part]:
			cp = parts.copy()
			cp[i] = replacement
			variations.add("".join(cp))
	return len(variations)

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')