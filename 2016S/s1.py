from collections import Counter

word = Counter(input())
card = Counter(input())

wildcard = True

for k in card:
    if k == "*":
        continue

    if k not in word:
        wildcard = False
        break
    elif card[k]>word[k]:
        wildcard = False
        break

if wildcard:
    print("A")
else:
    print("N")
