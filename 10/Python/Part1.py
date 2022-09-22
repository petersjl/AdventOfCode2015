from pathlib import Path
from time import perf_counter as timer

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = path.open().read()
	return input

def main():
	input = parseInput()
	for _ in range(40):
		input = expand(input)
	print(f'Expanded string is {len(input)} chars long')
	return

def expand(message:str) -> str:
	newMessage = ""
	current = message[0]
	count = 1
	for i in range(1, len(message)):
		c = message[i]
		if c == current:
			count += 1
			continue
		else:
			newMessage += str(count) + current
			current = c
			count = 1
	newMessage += str(count) + current
	return newMessage

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')