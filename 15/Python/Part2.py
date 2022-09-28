from pathlib import Path
import re
from time import perf_counter as timer

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = list(map(lambda s: re.split(": |, | ", s.strip()), path.open().read().split('\n')))
	ingredients:list[Ingredient] = []
	for x in input:
		ingredients.append(Ingredient(x[0], int(x[2]), int(x[4]), int(x[6]), int(x[8]), int(x[10])))
	return ingredients

class Ingredient:
	def __init__(self, name:str, cap:int, dur:int, fla:int, tex:int, cal:int) -> None:
		self.name = name
		self.capacity = cap
		self.durability = dur
		self.flavor = fla
		self.texture = tex
		self.calories = cal

def main():
	ingredients = parseInput()
	total = 100
	desiredCals = 500
	(bestScore, bestAmounts) = findRecipe(ingredients, total, [], desiredCals)
	print(f'\nBest score is {bestScore} with amounts')
	for i in range(len(ingredients)):
		print(f'{ingredients[i].name}: {bestAmounts[i]}')
	return

def findRecipe(ingredients:list[Ingredient], total:int, amounts:list[int], desiredCals:int) -> tuple[int, list[int]]:
	amountLeft = total - sum(amounts)
	if amountLeft < 0: print('shit broke')
	if  len(amounts) == 3: 
		amounts.append(amountLeft)
		return (calculateScore(ingredients, amounts, desiredCals), amounts)
	localMaxScore = -1
	localMaxAmounts = []
	for n in range(amountLeft + 1):
		newAmounts = amounts.copy()
		newAmounts.append(n)
		(currentScore, currentBest) = findRecipe(ingredients, total, newAmounts, desiredCals)
		if currentScore > localMaxScore:
			localMaxScore = currentScore
			localMaxAmounts = currentBest
	return (localMaxScore, localMaxAmounts)

def calculateScore(ingredients:list[Ingredient], amounts:list[int], desiredCals:int) -> int:
	cap = 0
	dur = 0
	fla = 0
	tex = 0
	cal = 0
	for i in range(len(ingredients)):
		cap += (ingredients[i].capacity*amounts[i])
		dur += (ingredients[i].durability*amounts[i])
		fla += (ingredients[i].flavor*amounts[i])
		tex += (ingredients[i].texture*amounts[i])
		cal += (ingredients[i].calories*amounts[i])
	if cal != desiredCals: return 0
	if cap < 0: cap = 0
	if dur < 0: dur = 0
	if fla < 0: fla = 0
	if tex < 0: tex = 0
	return (cap * dur * fla * tex)

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')