from pathlib import Path
import re
from time import perf_counter as timer

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = list(map(lambda s: re.split(", | ", s.strip()), path.open().read().split('\n')))
	return input

def main():
	instructions = parseInput()
	a = 0
	b = 0
	i = 0
	while True:
		(i, a, b) = processInstruction(i, instructions, a, b)
		if i >= len(instructions): break
	print(f'b ends with a value of {b}')
	return

def processInstruction(index:int, instructions:list[list[str]], a:int, b:int) -> tuple[int,int,int]:
	ins = instructions[index]
	if ins[0] == 'hlf':
		if ins[1] == 'a': return (index + 1, a / 2, b)
		else: return (index + 1, a, b / 2)
	elif ins[0] == 'tpl':
		if ins[1] == 'a': return (index + 1, a * 3, b)
		else: return (index + 1, a, b * 3)
	elif ins[0] == 'inc':
		if ins[1] == 'a': return (index + 1, a + 1, b)
		else: return (index + 1, a, b + 1)
	elif ins[0] == 'jmp': return (index + int(ins[1]), a, b)
	elif ins[0] == 'jie':
		if ins[1] == 'a': return (index + (1 if a % 2 != 0 else int(ins[2])), a, b)
		else: return (index + (1 if b % 2 != 0 else int(ins[2])), a, b)
	elif ins[0] == 'jio':
		if ins[1] == 'a': return (index + (1 if a != 1 else int(ins[2])), a, b)
		else: return (index + (1 if b != 1 else int(ins[2])), a, b)
	return

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')