#Pretty Average Primes

times = int(input())

def isPrime(N):
    if N == 1:
        return False
    elif N <=3:
        return True

    i = 2
    while (i*i<=N):
        if N%i==0:
            return False
        i+=1
    return True

for i in range(times):
    currNum = int(input())
    for j in range(currNum):
        if isPrime(j) and isPrime(currNum*2-j):
            print(str(j) + " " + str(currNum*2-j))
            break



