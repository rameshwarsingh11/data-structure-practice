# Graph implementation using Adjacency list provides more space efficient data structure for storing sparse matrices
# Adjacency List in Python to implement a Graph
class Vertex:

  def __init__(self, key):
    self.id = key
    self.connectedTo = {}

  def addNeighbour(self, nbr, weight=0):
    self.connectedTo[nbr] = weight

  def getConnections(self):
    return self.connectedTo.keys()

  def getVertexWeight(self,nbr=1):
    return self.connectedTo[nbr].weight

  def getId(self):
    return self.id

  def getWeight(self, nbr):
    return self.connectedTo[nbr]

  # Special method
  def __str__(self):
    return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])


class Graph:

  def __init__(self):
    self.vertList = {}
    self.numVertices = 0

  def addVertex(self, key):
    self.numVertices += 1
    newVertex = Vertex(key)
    self.vertList[key] = newVertex
    return newVertex

  def getVertex(self, n):
    if n in self.vertList:  # Iterate on Keys
      return self.vertList[n]

    else:
      return None

  def addEdge(self, f, t, cost=0):  # f= from vertex, t = to vertex, c= cost/weight
    if f not in self.vertList:
      nv = self.addVertex(f)
      if t not in self.vertList:
        nv = self.addVertex(t)

      self.vertList[f].addNeighbour(self.vertList[t], cost)

  def getVertices(self):
    return self.vertList.keys()

  # Special method
  def __iter__(self):
    return iter(self.vertList.values())

  def __contains__(self, n):
    return n in self.vertList


graph = Graph()
for i in range(10):
  graph.addVertex(i)

graph.vertList
graph.addEdge(0, 1, 45)
graph.addEdge(1, 2, 50)
graph.addEdge(0, 2, 55)
for vertex in graph:  
    print(vertex)
    print(vertex.getConnections())
    print(vertex.getVertexWeight())
    print('\n')
