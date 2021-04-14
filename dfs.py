# DFS implementation in Python
graph = {'A': set(['B','C']),
         'B': set(['A','D','E']),
         'C': set(['A','F']),
         'D': set(['B']),
         'E': set(['B','F']),
         'F': set(['C','E']),
}

def dfs(graph,start):
  already_visited = set()
  stack =[start]

  while stack:
    vertex = stack.pop()
    if vertex not in already_visited:
      already_visited.add(vertex)
      stack.extend(graph[vertex]- already_visited)

  return already_visited

print(dfs(graph,'A'))