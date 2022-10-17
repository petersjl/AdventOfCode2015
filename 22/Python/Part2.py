from __future__ import annotations
from pathlib import Path
from time import perf_counter as timer

class Entity:
	def __init__(self, hp:int, armor:int = 0) -> None:
		self.hp = hp
		self.armor = armor

	def takeAttack(self, damage:int) -> None:
		self.hp -= (damage - self.armor) if damage > self.armor else 1

class Mage(Entity):
	def __init__(self, hp:int, armor:int = 0, mana:int = 0) -> None:
		super().__init__(hp, armor)
		self.mana = mana
		self.spells = []
		self.spells.append(Spells.Missile)
		self.spells.append(Spells.Drain)
		self.spells.append(Spells.Shield)
		self.spells.append(Spells.Poison)
		self.spells.append(Spells.Recharge)

	def copy(self) -> Mage:
		return Mage(self.hp, self.armor, self.mana)

class Boss(Entity):
	def __init__(self, hp:int, armor:int = 0, attack:int = 0) -> None:
		super().__init__(hp, armor)
		self.attack = attack

	def copy(self) -> Boss:
		return Boss(self.hp, self.armor, self.attack)

class Effect:
	def __init__(self, duration:int, name:int) -> None:
		self.duration = duration
		self.name = name

	def __eq__(self, __o: object) -> bool:
		return self.name == __o.name

	def __str__(self) -> str:
		return f'({self.name}, {self.duration})'

	def __repr__(self) -> str:
		return f'({self.name}, {self.duration})'

	def copy(self) -> Effect:
		return Effect(self.duration, self.name)

	@staticmethod
	def copyList(effects:list[Effect]) -> list[Effect]:
		newEffects:list[Effect] = list()
		for e in effects:
			newEffects.append(e.copy())
		return newEffects

class Effects:
	Shield = 0
	Poison = 1
	Recharge = 2

class Spells:
	Missile = 53
	Drain = 73
	Shield = 113
	Poison = 173
	Recharge = 229

def parseInput() -> Boss:
	path = Path(__file__).parent / "../input.txt"
	input = path.open().read().split("\n")
	line = input[0].split(": ")
	hp = int(line[1])
	line = input[1].split(": ")
	damage = int(line[1])
	return Boss(hp, attack=damage)

def main():
	boss = parseInput()
	player = Mage(50, 0, 500)
	(mana, spells) = processTurn(player, boss, list(), 0)
	print(f'It takes a minimum of {mana} mana to beat the boss')
	print(spells)
	return

def processTurn(player:Mage, boss:Boss, effects:list[Effect], level, isPlayerTurn = True) -> tuple[int, list]:
	if isPlayerTurn:
		player.hp -= 1
		if player.hp <= 0: return (-1, [])
	processEffects(player, boss, effects)
	if player.hp <= 0 or player.mana <= 0 or player.mana > 10000: return (-1, [])
	if boss.hp <= 0: return (0, [(0, boss.hp)])
	low = 10 ** 9
	lowspells = []
	if not isPlayerTurn:
		player.takeAttack(boss.attack)
		return processTurn(player, boss, effects, level, True)
	for spell in player.spells:
		if spell == Spells.Missile:
			if player.mana - Spells.Missile < 0: continue
			pc = player.copy()
			bc = boss.copy()
			pc.mana -= Spells.Missile
			bc.takeAttack(4)
			(mana, spells) = processTurn(pc, bc, Effect.copyList(effects), level + 1, False)
			if mana < 0: continue
			mana += Spells.Missile
			if mana < low: 
				low = mana
				spells.insert(0, (Spells.Missile, bc.hp))
				lowspells = spells
		elif spell == Spells.Drain:
			if player.mana - Spells.Drain < 0: continue
			pc = player.copy()
			bc = boss.copy()
			pc.mana -= Spells.Drain
			bc.takeAttack(2)
			pc.hp += 2
			(mana, spells) = processTurn(pc, bc, Effect.copyList(effects), level + 1, False)
			if mana < 0: continue
			mana += Spells.Drain
			if mana < low: 
				low = mana
				spells.insert(0, (Spells.Drain, bc.hp))
				lowspells = spells
		elif spell == Spells.Shield:
			if player.mana - Spells.Shield < 0: continue
			newEffect = Effect(6, Effects.Shield)
			if newEffect in effects: continue
			pc = player.copy()
			bc = boss.copy()
			ec = Effect.copyList(effects)
			ec.append(newEffect)
			pc.mana -= Spells.Shield
			(mana, spells) = processTurn(pc, bc, ec, level + 1, False)
			if mana < 0: continue
			mana += Spells.Shield
			if mana < low: 
				low = mana
				spells.insert(0, (Spells.Shield, bc.hp))
				lowspells = spells
		elif spell == Spells.Poison:
			if player.mana - Spells.Poison < 0: continue
			newEffect = Effect(6, Effects.Poison)
			if newEffect in effects: continue
			pc = player.copy()
			bc = boss.copy()
			ec = Effect.copyList(effects)
			ec.append(newEffect)
			pc.mana -= Spells.Poison
			(mana, spells) = processTurn(pc, bc, ec, level + 1, False)
			if mana < 0: continue
			mana += Spells.Poison
			if mana < low: 
				low = mana
				spells.insert(0, (Spells.Poison, bc.hp))
				lowspells = spells
		elif spell == Spells.Recharge:
			if player.mana - Spells.Recharge < 0: continue
			newEffect = Effect(5, Effects.Recharge)
			if newEffect in effects: continue
			pc = player.copy()
			bc = boss.copy()
			ec = Effect.copyList(effects)
			ec.append(newEffect)
			pc.mana -= Spells.Recharge
			(mana, spells) = processTurn(pc, bc, ec, level + 1, False)
			if mana < 0: continue
			mana += Spells.Recharge
			if mana < low: 
				low = mana
				spells.insert(0, (Spells.Recharge, bc.hp))
				lowspells = spells
	return (low, lowspells)

def processEffects(player:Mage, boss:Boss, effects:list[Effect]) -> None:
	i = 0
	player.armor = 0
	while i < len(effects):
		effect = effects[i]
		if effect.name == Effects.Shield: player.armor = 7
		elif effect.name == Effects.Poison: boss.hp -= 3
		elif effect.name == Effects.Recharge: player.mana += 101
		effect.duration -= 1
		if effect.duration <= 0:
			effects.remove(effect)
			continue
		i += 1

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')