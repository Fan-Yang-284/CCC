# Street Sprinter
lines = int(input())
maxSpeed = -1.0
places = []

for i in range(lines):
    line = input().split(" ")
    places.append([int(line[0]), int(line[1])])

places.sort()

for i in range(len(places)-1):
    distance = abs(places[i+1][1] - places[i][1])
    time = abs(places[i+1][0] - places[i][0])
    speed = distance/time
    if speed>maxSpeed:
        maxSpeed = speed

print(maxSpeed)
