from pathlib import Path
from time import perf_counter as timer
from tkinter import E
from urllib.request import OpenerDirector

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = path.open().read().split("\n")
	nodes = set()
	edges = set()
	# get set of nodes and edges
	for s in input:
		parts = s.split(" ")
		nodes.add(parts[0])
		nodes.add(parts[2])
		edges.add(Edge(int(parts[4]), parts[0], parts[2]))
	nodelist = []
	nodelist.extend(nodes)
	edgelist = []
	edgelist.extend(edges)
	distances = [[0]*len(nodelist) for _ in range(len(nodelist))]
	for edge in edgelist:
		i1 = nodelist.index(edge.first)
		i2 = nodelist.index(edge.second)
		distances[i1][i2] = edge.distance
		distances[i2][i1] = edge.distance
	print(nodelist)
	i = 0
	numList = []
	for n in nodelist:
		numList.append(i)
		i += 1
	return (numList, distances)

def main():
	(nodes, distances) = parseInput()
	memo = {}
	for n in nodes:
		memo[n] = {}
	maximum = 0

	for n in nodes:
		cpy = nodes.copy()
		cpy.remove(n)
		maximum = max(maximum, tsp(n, cpy, distances, memo))
	print(f'The max distance is {maximum}')
	return

def tsp(i:int, nodes:list, dist, memo:dict) -> int:
	# base case where nodes has one item
	if len(nodes) == 1:
		return dist[i][nodes[0]]

	# check if we've already done this
	check = memo[i].get(toString(nodes))
	if check != None: return check

	#check all subsets for best
	maximum = 0
	for node in nodes:
		copy = nodes.copy()
		copy.remove(node)
		maximum = max(maximum, tsp(node, copy, dist, memo) + dist[node][i])

	# save best for this subset
	memo[i][toString(nodes)] = maximum
	return maximum

def toString(l):
	string = ""
	for s in l:
		string += str(s)
	return string

class Edge:
	distance: int
	first: str
	second: str

	def __init__(self, distance: int, first: str, second: str):
		self.distance = distance
		self.first = first
		self.second = second

	def __hash__(self):
		return hash((self.distance, self.first, self.second))

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')