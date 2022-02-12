import math
target = int(input())
res = ""
if target<10**5:
    print(target)
    res = ""
    for i in range(target):
        res+="1 "
    print(res[:-1])
    
else:
    correct = False
    for i in range(2,math.ceil(math.sqrt(target))):
        if target%(i+1) == i and (math.floor(target/(i+1)) + i)<=10**5:
            count = int(math.floor(target/(i+1)) + i)
            for j in range(0, count-i):
                res+="1 "
            for j in range(i):
                res+="2 "
                
            print(count)
            print(res[:-1])
            
            correct = True
            break     

    if not correct:
        print("Sad Chris")