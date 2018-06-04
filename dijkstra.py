import sys
import heapq

class Edge(object):

  def __init__(self, weight, startVertex, tragetVertex):
    self.weight = weight
    self.startVertex = startVertex
    self.tragetVertex = tragetVertex

class Node(object):

  def __init__(self, name):
    self.name = name
    self.visited = False
    self.predecessor = None
    self.adjacenciesList = []
    self.minDistance = sys.maxsize # max value

  def __cmp__(self, otherVertex):
    # сравнение экземпляров пользовательских типов
    return self.cmp(self.minDistance, otherVertex.minDistance)

  def __lt__(self, other):
    # проверку на «меньше чем» для экземпляров пользовательских типов
    selfPriority = self.minDistance
    otherPriority = other.minDistance
    return selfPriority < otherPriority
