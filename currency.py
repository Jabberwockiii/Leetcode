# USD,CAD,1.3;USD,GBP,0.71;USD,JPY,109;GBP,JPY,155
# USD
# JPY
# 0.71 * 155 = 110.05
l1 = "USD,CAD,1.3;USD,GBP,0.71;USD,JPY,109;GBP,JPY,155;CAD,CNY,6.9;GBP,CNY,20;CNY,JPY,20"
l2 = "USD"
l3 = "XYZ"
s = l1.split(";")
cleaned = []
for i in s:
    cleaned.append(i.split(","))
# construct a graph to represent the currency exchange rate 
# and find the longest path from USD to JPY
# edge is the exchange rate
# node is the currency name
# start from USD
class Graph:
    def __init__(self):
        self.graph = {}
        self.maxProd = -1
    def addEdge(self,u,v,w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v,w))
        self.graph[v].append((u,round(1/w,5)))
    def findLongestPath(self,start,end):
        visited = []
        queue = [(start,1)]
        while queue:
            node, currency = queue.pop(0)
            if node not in visited or node == end:
                visited.append(node)
                if node == end:
                    self.maxProd = max(self.maxProd, currency)
                for n,w in self.graph[node]:
                    if n not in visited or n == end:
                        queue.append((n,currency*w))
        return -1
g = Graph()
for i in cleaned:
    g.addEdge(i[0],i[1],float(i[2]))
print(g.graph)
g.findLongestPath("USD","CNY")
print(g.maxProd)