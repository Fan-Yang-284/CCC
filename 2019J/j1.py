# Winning Score
apples = []
bananas = []
sumApples = 0
sumBananas = 0

for i in range(3):
    apples.append(int(input()*(3-i)))
for i in range(3):
    bananas.append(int(input()*(3-i)))

sumApples = sum(apples)
sumBananas = sum(bananas)

if sumApples>sumBananas:
    print("A")
elif sumBananas>sumApples:
    print("B")
else:
    print("T")