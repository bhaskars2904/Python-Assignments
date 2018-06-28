import re
import random

def getGraph():
    """
    Input: text file with input
    Output: Returns a graph of 'dict' type
    """
    graph = {}
    f = open('kargerMinCut.txt')
    lines = f.readlines()
    f.close()
    #Removes multiple whitespaces(replce with one whitespace), newlines and whitespaces at end
    lines = map(lambda x: re.sub('\s+',' ',str(x.strip('\r\n'))).strip(),lines)
    #Splits at whitespaces
    lines = map(lambda x: x.split(' '),lines)
    #assigns the value(lsit) for key(first number of a line)
    for line in lines:
        graph[int(line[0])] = map(lambda x: int(x),line[1:])
    
    return graph

def contractEdge(edge, graph):
    """
    Input: edge, a list of two integers. graph, a dictionary with list as value
    Output: Returns nothing
    """
    #Removes edge[1] and puts its contents to edge[0]    
    v1 = graph[edge[0]]
    v1.extend(graph[edge[1]])
    del graph[edge[1]]
    #Replaces all mentions of edge[1] with edge[0]
    for k in graph:
        for x in range(len(graph[k])):
            if graph[k][x]==edge[1]:
                graph[k][x]=edge[0]
    #Removes all loops at edge[0]  
    for x in range(len(graph[edge[0]])-1,-1,-1):
        if graph[edge[0]][x]==edge[0]:
            del graph[edge[0]][x]

def getRandomEdge(graph):
    """
    Input: graph, a dictionary with list as value
    Output: a list of two integers
    """
    #Generates a random key of graph    
    v1 = graph.keys() [random.randint(0,len(graph)-1)]    
    #Generates a random index of list at the above key of graph    
    v2 = graph[v1][random.randint(0,len(graph[v1])-1)]
    return (v1,v2)

#minCut keeps all the minimum cuts from all the iterations    
minCut = []

for i in xrange(0,20):
    graph = getGraph()
    while(len(graph) > 2):
        contractEdge(getRandomEdge(graph),graph)
    
    minCut.append(len(graph[graph.keys()[0]]))
print "The minimum cut from above randomized algorithm is "+str(min(minCut))
