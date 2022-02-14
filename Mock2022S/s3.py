# Absolutely Acidic

from collections import Counter

N = int(input())
readings = []
for i in range(N):
    readings.append(int(input()))

readings = Counter(readings)

m1,m2 = 0,0

max1 = []
max2 = []

for k,v in readings.items():
    if v>m1:
        m2 = m1
        m1 = v
        max2 = max1
        max1 = [k]
    elif v>m2:
        m2 = v
        max2 = [k]
    elif v==m1:
        max1.append(k)
    elif v == m2:
        max2.append(k)

if len(max1)>=2:
    print(max(max1)-min(max1))
elif len(max1) == 1:
    print(max( abs(max(max1)-min(max2)),abs(min(max1)-max(max2)) )) 
