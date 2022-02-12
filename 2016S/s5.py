from sys import stdin
input = stdin.readline

N,T = map(int,input()[:-1].split(" "))

cells = input()[:-1]
newCells = ['']*N
# print((N,T))
# print(cells)

intervals = [n for n in range(T+1) if n%2==T%2]

# whether or not cell is alive is equal after T generations to XOR of (cell-T) mod n, (cell + T) mod n
for i in range(N):
    count1=0
    count0=0
    for j in intervals:
        l = (i-j)%N
        r = (i+j)%N
        #print((l,r))
        if cells[l] == '1':
            count1+=1
        if cells[r] == '1':
            count1+=1
    if T%2 == 0:
        if count1 == T/2 :
            newCells[i] = '1'
        else:
            newCells[i] = '0'
    else:
        if count1%2 == 1:
            newCells[i] = '1'
        else:
            newCells[i] = '0'

print("".join(newCells))