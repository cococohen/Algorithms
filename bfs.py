graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs(graph, start):
	visited = set()
	stack = [start]
	while stack:
		vertex = stack.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex]-visited)
			print vertex
			print visited
			print stack
	#print visited
	
bfs(graph, 'A')
