from pathlib import Path
from time import perf_counter as timer

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = path.open().read().split("\n")
	i = 0
	conversions = dict[str, str]
	conversions = dict()
	while input[i] != "":
		line = input[i].split(" => ")
		if conversions.get(line[1]) != None: 
			print("Duplicate conversion")
			exit(1)
		conversions[line[1]] = line[0]
		i += 1
	molecule = input[i + 1]
	return (conversions, molecule)

def main():
	(conversions, molecule) = parseInput()
	count = reduceToE(conversions, molecule)
	print(f'The medicine can be made in {count} steps')
	return

def reduceToE(conversions:dict[str, str], molecule:str) -> int:
	queue = PriorityQueue()
	queue.enqueue((molecule, 0))
	seen = set()
	while len(queue) != 0:
		(current, depth) = queue.dequeue()
		seen.add(current)
		newMolecules = reduce(conversions, current)
		newDepth = depth + 1
		for mol in newMolecules:
			if len(mol) == 1 and mol == "e": return newDepth
			if "e" in mol: continue
			if mol not in seen: queue.enqueue((mol, newDepth))
	return -1

def reduce(conversions:dict[str, str], molecule:str) -> list[str]:
	mols = set()
	for con in conversions.keys():
		if con in molecule:
			i = 0
			while True:
				mol = replace(molecule, con, conversions[con], i)
				if mol == None: break
				mols.add(mol)
				i += 1
	return list(mols)

class PriorityQueue:
	def __init__(self) -> None:
		self.__queue = []

	def __len__(self):
		return len(self.__queue)

	def enqueue(self, val:tuple[str, int]) -> None:
		for i in range(len(self.__queue)):
			match self.__compare(val, self.__queue[i]):
				case 1 : continue
				case 0 : return # same value so ignore it
				case -1 : 
					self.__queue.insert(i, val)
					return
		self.__queue.append(val)

	def dequeue(self) -> tuple[str,int]:
		return self.__queue.pop(0)

	def __compare(self, t1:tuple[str,int], t2:tuple[str,int]) -> int:
		if len(t1[0]) < len(t2[0]): return -1
		if len(t1[0]) > len(t2[0]): return 1
		if t1[1] < t2[1]: return -1
		if t1[1] > t2[1]: return 1
		return 0

def replace(string:str, old:str, new:str, skip:int) -> str | None:
	i = 0
	index = 0
	while i < skip:
		try:
			index = string.index(old, index)
			index +=1
			i += 1
		except ValueError:
			return None
	if(index >= len(string)): return None
	first = string[:index]
	second = string[index:].replace(old,new,1)
	return first + second

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')