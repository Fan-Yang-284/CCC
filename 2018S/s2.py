#Voronoi Villages
lines = int(input())

villages = []

for i in range(lines):
    villages.append(int(input()))

villages.sort()

distance = (villages[1]-villages[0])/2 + (villages[2] - villages[1])/2

for i in range(1,lines-1):
    curDistance = (villages[i]-villages[i-1])/2 + (villages[i+1] - villages[i])/2
    if curDistance<distance:
        distance = curDistance

distance = round(distance,1)

print(distance)