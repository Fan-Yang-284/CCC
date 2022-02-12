[N,W,D] = [int(n) for n in input().split(" ")]
N = int(N)
W = int(W)
D = int(D)
for value in [N,W,D]:
    value = int(value)

walkways = {}

for i in range(W):
    walkway = input().split(" ")
    walkways[int(walkway[0])] = int(walkway[1])

#print(walkways)
stations = [int(num) for num in input().split(" ")] # permutation of stations (station numbers)

positions = {} # dict that stores the position of the stations (Ex: 1 3 2 4 => {1: 1, 2: 3, 3: 2, 4: 4}) (Station indices)

for i in range(len(stations)):
    positions[stations[i]] = i+1

swaps = []

for i in range(D):
    swaps.append([int(num) for num in input().split(" ")])
#print(swaps)

while len(swaps)!=0:
    curr = swaps.pop(0)
    #getting station numbers to be swapped
    station1 = stations[curr[0]-1]
    station2 = stations[curr[1]-1]
    #print((station1,station2))

    # performing swap
    stations[positions[station2]-1] = station1 #change index of station2 value to value of station1
    stations[positions[station1]-1] = station2 #change index of station1 value to value of station2

    #update station indices
    temp = positions[station1] 
    positions[station1] = positions[station2]
    positions[station2] = temp

    #print(stations)
    #print(positions)

    #BFS to find shortest time needed
    minTime = -1
    BFS = [(1,0)] # stores tuples of (current position (index) in line of stations, current time)
    
    dp = [0] * len(stations) # memoize

    for i in range(len(stations)):
        dp[stations[i]-1] = i

    while len(BFS)!=0:
        #print(BFS)
        currNode = BFS.pop(0)
        
        ##print(currNode)
        # if current time > station before current station means there was faster way to get here so not optimal, pass
        if currNode[1]>dp[currNode[0]-1]:
            continue
        elif currNode[1]<dp[currNode[0]-1]:
            dp[currNode[0]-1] = currNode[1]

        elif stations[currNode[0]-1] == N:
            print(currNode[1])
            break
        
        elif currNode[0] not in walkways and currNode[1] > positions[currNode[0]]: # no one way walkways to access and you are behind the train (current time greater than current position)
            # a deadend
            #print("A")
            continue

        elif currNode[0] in walkways and currNode[1] >= positions[currNode[0]]: # have an accessible walkway but currently behind the train
            #print("B")
            BFS.append((positions[walkways[currNode[0]]], currNode[1]+1)) #add walkway ending indice, currtime+1
        
        elif currNode[0] not in walkways and currNode[1] < positions[currNode[0]]: # have no walkways, but at or ahead of train
            if currNode[1]+1 == positions[currNode[0]]: # you can board the train to go to the next station in the line of stations
                #print("CA")
                BFS.append((currNode[0]+1,currNode[1]+1))
            else: # no walkways, but you can wait for a train to arrive
                #print("CB")
                BFS.append((currNode[0], currNode[1]+1))
        
        else: # can both access a walkway and access/wait for a train
            BFS.append((positions[walkways[currNode[0]]] ,currNode[1]+1))
            #if current time is equal to the time that train would arrive
            if currNode[1]==positions[currNode[0]]-1: # you can board the train to go to the next station in the line of stations
                BFS.append((currNode[0]+1,currNode[1]+1))
                #print("DA")
            else: # no walkways, but you can wait for a train to arrive
                BFS.append((currNode[0], currNode[1]+1))
                #print("DB")