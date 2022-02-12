# High Tide, Low Tide
import math
nums = int(input())
line = input().split(" ")

for i in range(len(line)):
    line[i] = int(line[i])

line = sorted(line)
res = ""

if nums%2 == 0:
    nums/=2
    nums = int(nums)
    for i in range(nums):
        if not i+1 == nums:
            res += str(line[nums-i-1]) + " " + str(line[nums+i]) + " "
        else:
            res += str(line[0]) + " " + str(line[-1])

else:
    nums = int(math.floor(nums/2))

    for i in range(nums):
        res += str(line[nums-i-1]) + " " + str(line[nums+i+1]) + " "
    res += str(line[nums])


print(res)
