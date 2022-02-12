# Secret Instructions
curr = "right"
while True:
    line = input()
    if line == "99999":
        break

    if line[0:2] == "00":
        print(curr+" "+line[2:])
    
    elif (int(line[0]) + int(line[1]))%2==0:
        curr = "right"
        print(curr+" "+line[2:])
    else:
        curr = "left"
        print(curr+" "+line[2:])