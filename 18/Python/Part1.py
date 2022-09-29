from pathlib import Path
from time import perf_counter as timer

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = path.open().read().split('\n')
	lights = []
	for line in input:
		string = []
		for light in line:
			string.append(light == "#")
		lights.append(string)
	return lights

def main():
	lights = parseInput()
	iterations = 100
	for _ in range(iterations):
		lights = getNextState(lights)
	count = countLightsOn(lights)
	#printLights(lights)
	print(f'After {iterations} iterations, {count} lights were on')
	return

def getNextState(lights:list[list[bool]]) -> list[list[bool]]:
	newLights = []
	for x in range(len(lights)):
		newLine = []
		for y in range(len(lights[0])):
			newLine.append(getNextLight(lights, x, y))
		newLights.append(newLine)
	return newLights

def getNextLight(lights:list[list[bool]], x:int, y:int) -> bool:
	neighborsOn = 0
	for i in [x-1,x,x+1]:
		if i < 0 or i == len(lights): continue
		for j in [y-1,y,y+1]:
			if j < 0 or j == len(lights[0]): continue
			if i==x and j==y: continue
			if lights[i][j]: neighborsOn += 1
	return (1 < neighborsOn < 4) if lights[x][y] else neighborsOn == 3

def countLightsOn(lights:list[list[bool]]) -> int:
	count = 0
	for row in lights:
		for val in row:
			if val: count += 1
	return count

def printLights(lights):
	count = 0
	for row in lights:
		line = ""
		for val in row:
			line += "#" if val else "."
		print(line)

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')