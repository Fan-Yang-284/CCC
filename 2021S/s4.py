# Daily Commute 
from collections import defaultdict as dd
from sys import stdin
input = stdin.readline
[N,W,D] = [int(n) for n in input()[:-1].split(" ")]

walkways = dd(list)

for i in range(W):
    walkway = [int(n) for n in input()[:-1].split(" ")]
    walkways[walkway[1]].append(walkway[0])

stations = [int(n) for n in input()[:-1].split(" ")] # permutation of stations (station numbers)

positions = {} # dict that stores the position of the stations (Ex: 1 3 2 4 => {1: 1, 2: 3, 3: 2, 4: 4}) (Station indices)

for i in range(len(stations)):
    positions[stations[i]] = i+1

"""
Insight: walkways are not faster than bus unless path is only walkways, as otherwise have to wait for bus anyways
*actually you could ride bus to any given station then use walkways to get to end

Algorithm:
compute bus time from 1 to N (worst case scenario)
start at N (target station)
for every station accessible by N,
    edge case 1) if station already visited, continue
    ec 2) if station is 1, this is shortest time
    ec 3) time taken to get to this walkway bigger than worst case: break and just return
    a) compute bus time from station to 1, see if lower
    b) look at every other station accessible from walkway, and repeat

"""

for i in range(D):
    curr = [int(num) for num in input()[:-1].split(" ")] #get each swap
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

    minTime = positions[N] - positions[1]

    #BFS to find shortest time needed using pathways
    BFS = [(N,0)] # stores tuples of (current position (index) in line of stations, current time)

    visited = set()

    while BFS:
        currNode = BFS.pop(0)
        if currNode[1]==minTime: 
            break #at this point no routes faster than current min/bus
        elif currNode[0] in visited: # since BFS, if already visited then must be slower than an existing route
            continue
        visited.add(currNode[0])
        #check if current station is target station
        minTime = min(minTime,currNode[1]+(positions[currNode[0]]-positions[1])) # see how long for bus from current station to station 1

        #BFS to check all other accessible stations via walkway
        for station in walkways[currNode[0]]: 
            BFS.append((station, currNode[1]+1))

    print(minTime)
