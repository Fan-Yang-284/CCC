# Cold Compress
lines = input()

for i in range(int(lines)):
    line = list(input())
    array = []
    output = ""
    if len(line)==0:
        continue
    currChar = line[0]
    counter = 1
    j = 0

    while(j<len(line)):       
        if len(line)==1:
            array.append([currChar, counter])
            break
        elif j+1 >= len(line):
            array.append([currChar, counter])
            break
        elif line[j+1] == currChar:
            counter+=1
            j+=1
        else:
            array.append([currChar, counter])
            currChar = line[j+1]
            counter=1
            j+=1
    
    for k in range(len(array)):
        output += (str(array[k][1]) + " " + array[k][0])
        if k != (len(array)-1):
            output += " "

    print(output)
        