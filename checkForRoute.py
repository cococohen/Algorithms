


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def checkForRoute(graph, start, finish):
	visited = set()
	stack = [start]
	
	while stack:
		vertex = stack.pop()
		if vertex == finish:
			return True
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)			
	print visited
	return False
	
print(checkForRoute(graph, 'C', 'A'))
