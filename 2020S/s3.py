# Searching for Strings
from sys import stdin
input = stdin.readline
needle = input()[:-1]
haystack = input()[:-1]
counter = 0

if len(needle)>len(haystack):
    print("0")
else:
    perms = set()
    chars = set(haystack)
    needleD = dict()
    haystackD = dict()

    for char in chars:
        needleD[char]=0
        haystackD[char]=0

    l,r = 0, len(needle)
    
    for i in range(r):
        haystackD[haystack[i]]+=1
        needleD[needle[i]]+=1

    while r<=len(haystack):
        if needleD == haystackD and haystack[l:r] not in perms:
            counter+=1
            perms.add(haystack[l:r])

        if r == len(haystack):
            break

        haystackD[haystack[l]]-=1
        haystackD[haystack[r]]+=1

        l+=1
        r+=1

    print(counter)