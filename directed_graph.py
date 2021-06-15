# Directed Graph in Python
# Using prebuilt OrderDict & enum classes

from enum import Enum
from collections import OrderedDict

class State(Enum):
  unvisited = 1
  already_visited = 2
  now_visiting = 3

class Node:
  def __init__(self, num):
    self.num = num
    self.visit_state = State.unvisited
    # An Ordered Dictionary maintains the order as well in which keys are inserted. This greatly helps in node search process.
    self.adjacent = OrderedDict()

  # Special method
  def __str__(self):
    return str(self.num)

class Graph:
  def __init__(self):
    self.nodes = OrderedDict()

  def add_node(self, num):
    node = Node(num)
    self.nodes[num] = node

  def add_edge(self, source, dest, weight=0):
    if source not in self.nodes:
      self.add_node(source)

    if dest not in self.nodes:
      self.add_node(dest)

    self.nodes[source].adjacent[self.nodes[dest]] = weight

graph = Graph()
graph.add_edge(0, 1, 6)
graph.add_edge(1, 2, 5)
print('Total nodes added =', graph.nodes.__len__())
