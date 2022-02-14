# Animal Farm
from sys import stdin
input = stdin.readline
N = int(input()[:-1])

pens = []

for i in range(N):
    pens.append(list(map(int,input()[:-1].split(" "))))

nodes = {}

for i in range(len(pens)):
    count = i+1 # arbitrary pen number
    edges = pens[i][0] # number of connections
    nodes[count] = [] # initialize adj list

    for j in range(1,edges+1):
        nodes[count].append( (tuple(sorted((pens[i][j], pens[i][(j%edges)+1]))), pens[i][j+edges]) ) # tuple containing tuple of two ends of edge, weight

#print(nodes)

# construct graph by looking at each connection in nodes:
# if connection is in another k,v pair: make that the common edge, construct graph
# if connection is not, then must be common edge with outside, construct graph
# then do MST to find total sum

# graph stores adj list, in the form of graph[0] = [(a,b)] where a is the neighbour pen, b is weight
added = set()
edges = []
connectedPens = set()
items = nodes.items()
#print(items)
for k,v in items:
    for connection in v:
        if connection in added:
            continue
        found = False
        for l,w in items:
            if found:break
            if l == k:
                continue
            elif connection in w:
                found = True
                if k>l:
                    edges.append([l,k,connection[1]])
                    connectedPens.add((l,k))
                else:
                    edges.append([k,l,connection[1]])
                    connectedPens.add((k,l))
        if not found:
            edges.append([0,k,connection[1]])
            connectedPens.add((0,k))
        added.add(connection)

edges = list(list(tuple) for tuple in set((tuple(sub) for sub in edges)))

edges.sort(key = lambda x:x[2])
#print(edges)
def MST():
    cost = 0
    treeIDs = []
    for k in range(N+1):
        treeIDs.append(k)
    count0 = 0
    weight0 = 0
    for edge in edges:
        if(treeIDs[edge[0]]!=treeIDs[edge[1]]):
            cost+=edge[2]
            if edge[0] == 0:
                weight0+=edge[2]
                count0+=1

            old,new = treeIDs[edge[0]], treeIDs[edge[1]]
            for i in range(N+1):
                if treeIDs[i] == old:
                    treeIDs[i] = new

    if count0==1:
        cost-=weight0
    
    return cost

print(MST())