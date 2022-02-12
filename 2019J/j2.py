# Time to Decompress
lines = int(input())

output = []

for i in range(lines):
    line = input().split()
    output.append([int(line[0]),line[1]])

for i in range(lines):
    print(output[i][1]*output[i][0])
