from pathlib import Path
from time import perf_counter as timer

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = list(map(lambda s: s.split(" "), path.open().read().split('\n')))
	reigndeerList = []
	for x in input:
		reigndeerList.append(Reigndeer(x[0], int(x[3]), int(x[6]), int(x[13])))
	return reigndeerList

class Reigndeer:
	def __init__(self, name:str, speed:int, run:int, rest:int) -> None:
		self.name = name
		self.speed = speed
		self.run = run
		self.rest = rest
		self.resting = False
		self.current = run
		self.distance = 0
		self.points = 0
	
	def advance(self):
		self.distance += self.speed if not self.resting else 0
		self.current -= 1
		if self.current == 0:
			self.current = self.run if self.resting else self.rest
			self.resting = not self.resting

def main():
	reigndeer:list[Reigndeer] = parseInput()
	time = 2503
	for _ in range(time):
		for r in reigndeer:
			r.advance()
		awardPoints(reigndeer)
	winner = findWinner(reigndeer)

	print(f'{winner.name} won by gaining {winner.points} points')
	return

def findWinner(reigndeer:list[Reigndeer]) -> Reigndeer:
	winner = reigndeer[0]
	for r in reigndeer:
		if r.points > winner.points:
			winner = r
	return winner

def awardPoints(reigndeer:list[Reigndeer]) -> None:
	farthest = reigndeer[0].distance
	for r in reigndeer:
		if r.distance > farthest:
			farthest = r.distance
	for r in reigndeer:
		if r.distance == farthest:
			r.points += 1

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')