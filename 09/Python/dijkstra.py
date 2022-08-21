from pathlib import Path
from time import perf_counter as timer
from tkinter import E
from urllib.request import OpenerDirector

def parseInput():
	path = Path(__file__).parent / "../input.txt"
	input = path.open().read().split("\n")
	nodes = set()
	edges = set()
	for s in input:
		parts = s.split(" ")
		nodes.add(parts[0])
		nodes.add(parts[2])
		edges.add(Edge(int(parts[4]), parts[0], parts[2]))
	nodelist = []
	nodelist.extend(nodes)
	edgelist = []
	edgelist.extend(edges)
	print(nodelist)
	return (nodelist, edgelist)

def main():
	(nodes, edges) = parseInput()
	seenNodes = []
	openEdges = []
	usedEdges = []
	# Get the first node and add it to seen
	currentNode = nodes.pop(0)
	seenNodes.append(currentNode)
	while len(nodes) != 0:
		print(f'Current node: {currentNode}')
		# Get any new edges that can be seen from the seen nodes and remove them from edges
		i = 0
		while i < len(edges):
			edge = edges[i]
			if edge.contains(currentNode):
				openEdges.append(edge)
				edges.remove(edge)
				continue
			i += 1
		
		# Sort the edges, get the smallest edge, and add it to the used edges
		openEdges.sort()
		newEdge = openEdges.pop(0)
		usedEdges.append(newEdge)
		# Set the newly seen node as current and add it to seen nodes
		if newEdge.first in seenNodes:
			currentNode = newEdge.second
		else:
			currentNode = newEdge.first
		seenNodes.append(currentNode)
		nodes.remove(currentNode)
		# Remove any edges contained within the current map
		i = 0
		while i < len(openEdges):
		# for edge in openEdges:
			edge = openEdges[i]
			if edge.contained(seenNodes):
				openEdges.remove(edge)
				continue
			i += 1
		print("")

	route = seenNodes[0]
	for i in range(1, len(seenNodes)):
		route += f' => {seenNodes[i]}'
	total = 0
	for edge in usedEdges:
		total += edge.distance
	print(f'Route: {route}')
	print(f'Distance: {total}')
	return

class Edge:
	distance: int
	first: str
	second: str

	def __init__(self, distance: int, first: str, second: str):
		self.distance = distance
		self.first = first
		self.second = second

	def __eq__(self, other):
		if not isinstance(other, Edge):
			return NotImplemented
		return self.distance == other.distance and ((self.first == other.first and self.second == other.second) or (self.first == other.second and self.second == other.first))

	def __hash__(self):
		return hash((self.distance, self.first, self.second))

	def __lt__(self, other):
		return self.distance < other.distance

	def __str__(self):
		return f'({self.distance}, {self.first}, {self.second})'

	def __repr__(self):
		return f'({self.distance}, {self.first}, {self.second})'

	def contains(self, other: str) -> bool:
		return self.first == other or self.second == other

	def contained(self, nodes:list) -> bool:
		return self.first in nodes and self.second in nodes

if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print(f'Ran in {end - start} seconds')