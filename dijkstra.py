import sys
import heapq

class Edge(object):

  def __init__(self, weight, startVertex, targetVertex):
    self.weight = weight
    self.startVertex = startVertex
    self.targetVertex = targetVertex

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

class Algorithm(object):

  def calculateShortestPath(self, vertexList, startVertex):

    queue = []
    startVertex.minDistance = 0
    heapq.heappush(queue, startVertex) # init heap in 'q'

    while len(queue) > 0:
      acturalVertex = heapq.heappop(queue) # get node with min distance

      for edge in acturalVertex.adjacenciesList:
        u = edge.startVertex
        v = edge.targetVertex
        newDistance = u.minDistance + edge.weight

        if newDistance < v.minDistance:
          v.predecessor = u
          v.minDistance = newDistance
          heapq.heappush(queue, v)

  def getShortestPathTo(self, targetVertex)
    print('Shortest path to vertex')

    node = targetVertex

    while node is not None:
      print('%s ' % node.name)
      node = node.predecessor

