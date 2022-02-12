from collections import defaultdict as dd

N,M = map(lambda x: int(x), input().split(" "))

phos = set(map(lambda x: int(x), input().split(" ")))

restaurants = set()

roads = dd(list)

for i in range(N-1):
    pair = tuple(map(lambda x: int(x), input().split(" ")))
    roads[pair[0]].append(pair[1])
    roads[pair[1]].append(pair[0])
    restaurants.add(pair[0])
    restaurants.add(pair[1])

# pick a random node
# if each of the pho restaurants are a leaf of the tree
# then that means that each branch of tree must be visited twice, or once (choose longest one)
visited = set()
BFS = [x for x in roads if len(roads[x])==1] # all current leaves of the tree

# algo is to continually move inwards, and stop if a pho restaurant is reached

while BFS:
    curr = BFS.pop(0)