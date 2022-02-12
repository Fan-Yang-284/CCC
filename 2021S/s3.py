# lunch concert
lines = int(input())

friends = []
#P = position, W = 1m every W seconds, D = Hearing Distance 
#indexes 0 , 1 , 2, respectively
maxP = -1

for i in range(lines):
    friends.append(input().split(" "))
    maxP = max(maxP,int(friends[-1][0])) # range of vals: 0 to maxP
    
def getTimes(people,concertPos):
    totalTime = 0
    for person in people:
        currPos = int(person[0]) # m number
        currSpeed = int(person[1])  # 1m / currSpeed seconds
        currHear = int(person[2]) # m distance
        if currPos == concertPos:
            continue
        elif concertPos>currPos:
            distanceNeeded = max(concertPos - currHear - currPos,0) # if overlap, negative
        else:
            distanceNeeded = max(currPos - concertPos - currHear,0) # if overlap, negative
        
        timeNeeded = distanceNeeded * currSpeed #somehow this works idk why

        totalTime += timeNeeded
    
    return totalTime

currTime = getTimes(friends,maxP//2)

leftTime = getTimes(friends,maxP//2-1)
rightTime = getTimes(friends,maxP//2+1)
l,r = 0, maxP

while(leftTime<currTime or rightTime<currTime):
    if leftTime>currTime: #left is higher, right is lower (limit search space to right half of curve)
        l = (l+r)//2
    else: # right is higher, left is lower (limit search space of left half of curve)
        r = (l+r)//2

    currTime = getTimes(friends,(l+r)//2) #get new time for halfway between new left, new right
    leftTime = getTimes(friends,(l+r)//2-1) #compare with left
    rightTime = getTimes(friends,(l+r)//2+1) #compare with right

print(currTime)
