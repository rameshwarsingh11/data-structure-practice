# Implementing Breadth First Search ( find the shortest path)
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         }


def bfs(graph, start):
  already_visited = set()
  queue = [start]

  while queue:
    vertex = queue.pop(0)
    if vertex not in already_visited:
      already_visited.add(vertex)
      queue.extend(graph[vertex]-already_visited)

  return already_visited


print(bfs(graph, 'A'))
