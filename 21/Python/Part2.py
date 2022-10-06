from pathlib import Path
from re import L
from time import perf_counter as timer

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = list(map(lambda s: s.split(": "), path.open().read().split('\n')))
	boss = {}
	for n in input:
		boss[n[0]] = int(n[1])
	return boss

def parseShop() -> dict[str, list]:
	path = Path(__file__).parent / "../shop.txt"
	input = path.open().read().split('\n\n')
	shop = {}
	weapons = []
	for item in input[0].split('\n')[1:]:
		line = item.split()
		weapon = {
			"name": line[0],
			"cost": int(line[1]),
			"damage": int(line[2])
			}
		weapons.append(weapon)
	shop["weapons"] = weapons
	armors = []
	for item in input[1].split('\n')[1:]:
		line = item.split()
		armor = {
			"name": line[0],
			"cost": int(line[1]),
			"armor": int(line[3])
			}
		armors.append(armor)
	shop["armor"] = armors
	rings = []
	for item in input[2].split('\n')[1:]:
		line = item.split()
		ring = {
			"name": line[0],
			"cost": int(line[1]),
			"damage": int(line[2]),
			"armor": int(line[3])
			}
		rings.append(ring)
	shop["rings"] = rings
	return shop

class Loadout:

	def __init__(self, maxRings = 0) -> None:
		self.maxRings = maxRings
		self.rings = []
		self.weapon = None
		self.armor = None
		self.cost = 0
		self.attack = 0
		self.defense = 0

	def __str__(self) -> str:
		string = f'Weapon: {self.weapon}\nArmor: {self.armor}\nRings:\n'
		for r in self.rings:
			string += f' {r}\n'
		string += f'A/D: {self.attack}/{self.defense}\n'
		string += f'Cost: {self.cost}'
		return string
	
	def registerWeapon(self, weapon:dict):
		if self.weapon != None: return
		self.weapon = weapon["name"]
		self.attack += weapon["damage"]
		self.cost += weapon["cost"]

	def registerArmor(self, armor:dict):
		if self.armor != None: return
		self.armor = armor["name"]
		self.defense += armor["armor"]
		self.cost += armor["cost"]

	def registerRing(self, ring:dict):
		if len(self.rings) == self.maxRings: return
		self.rings.append(ring["name"])
		self.attack += ring["damage"]
		self.defense += ring["armor"]
		self.cost += ring["cost"]

def main():
	boss = parseInput()
	shop  = parseShop()
	maxRings = 2 #currently won't work if changed
	(atk, dfn) = findMaxStats(shop, maxRings)
	low = findWeakestWeapon(shop)
	pairs = findValidStats(low, atk, dfn, boss)
	loadouts = findValidLoadouts(shop, pairs, maxRings)
	lowest = findHighestCostLoadout(loadouts)
	print(f'The highest cost loadout for a loss is:')
	print(lowest)
	return

def findHighestCostLoadout(loadouts:list[Loadout]) -> Loadout:
	if len(loadouts) == 0: return None
	highest:Loadout = loadouts[0]
	for l in loadouts:
		if l.cost > highest.cost: highest = l
	return highest

def findValidLoadouts(shop:dict[str, list], stats:list[tuple[int, int]], maxRings:int = 0) -> list[Loadout]:
	valid:list[Loadout] = []
	armor = shop["armor"].copy()
	armor.append({
			"name": "None",
			"cost": 0,
			"armor": 0
			})
	rings = shop["rings"].copy()
	for _ in range(maxRings):
		rings.append({
			"name": None,
			"cost": 0,
			"damage": 0,
			"armor": 0
			})
	for w in shop["weapons"]:
		for a in armor:
			# TODO: make this work for variable number of rings
			for r in rings:
				copy = rings.copy()
				copy.remove(r)
				for r2 in copy:
					l = Loadout(maxRings)
					l.registerWeapon(w)
					l.registerArmor(a)
					l.registerRing(r)
					l.registerRing(r2)
					if (l.attack, l.defense) in stats:
						valid.append(l)
	return valid

def findValidStats(minAtk:int, maxAtk:int, maxDfn:int, boss:dict[str,int]) -> list[tuple[int,int]]:
	pairs = []
	for a in range(minAtk, maxAtk + 1):
		for d in range(maxDfn + 1):
			player = {"HP": 100, "Damage": a, "Armor": d}
			clone = boss.copy()
			if simulateBattle(player, clone):
				pairs.append((a,d))
	return pairs

def findWeakestWeapon(shop:dict[str, list]):
	low = 1000
	for w in shop["weapons"]:
		if w["damage"] < low: low = w["damage"]
	return low

def findMaxStats(shop:dict[str, list], maxRings:int = 0):
	maxWeapon = 0
	for w in shop["weapons"]:
		if w["damage"] > maxWeapon: maxWeapon = w["damage"]
	maxArmor = 0
	for a in shop["armor"]:
		if a["armor"] > maxArmor: maxArmor = a["armor"]
	maxAtkRing = 0
	availRings:list = shop["rings"].copy()
	for _ in range(maxRings):
		curMax = 0
		bestRing = None
		for r in availRings:
			if r["damage"] > curMax:
				curMax = r["damage"]
				bestRing = r
		availRings.remove(bestRing)
		maxAtkRing += curMax
	maxDefRing = 0
	availRings:list = shop["rings"].copy()
	for _ in range(maxRings):
		curMax = 0
		bestRing = None
		for r in availRings:
			if r["armor"] > curMax:
				curMax = r["armor"]
				bestRing = r
		availRings.remove(bestRing)
		maxDefRing += curMax
	return (maxWeapon + maxAtkRing, maxArmor + maxDefRing)

def simulateBattle(player:dict[str,int], boss:dict[str,int]) -> bool:
	playerTurn = True
	while True:
		if playerTurn: 
			simulateAttack(player, boss)
			if boss["HP"] <= 0: return False
		else: 
			simulateAttack(boss, player)
			if player["HP"] <= 0: return True
		playerTurn = not playerTurn

def simulateAttack(attacker:dict[str,int], defender:dict[str,int]) -> None:
	atk = attacker["Damage"]
	dfn = defender["Armor"]
	defender["HP"] -= (atk - dfn) if atk > dfn else 1

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')