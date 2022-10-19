from pathlib import Path
from re import I
import re
from time import perf_counter as timer

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = re.split(", | |\.", path.open().read()) 
	row = int(input[input.index('row') + 1])
	col = int(input[input.index('column') + 1])
	return (row, col)

def main():
	(row, col) = parseInput()
	startVal = 20151125
	code = genCode(calcRowValAtCol(row, col), startVal)
	print(f'Code at {row}, {col} is {code}')
	return

def calcRowValAtCol(row:int, col:int) -> int:
	i = 1
	count = 1
	while i < col:
		i += 1
		count += i
	i = 1
	while i != row:
		count += col
		col += 1
		i += 1
	return count

def genCode(index:int, startVal:int) -> int:
	i = 1
	val = startVal
	while i < index:
		i += 1
		val *= 252533
		val %= 33554393
	return val

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')