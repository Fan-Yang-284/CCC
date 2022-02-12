# inputCase = """7
# 47 12 12 3 9 9 3""".splitlines()
# def input():
# 	global inputCase
# 	x = inputCase.pop(0)
# 	print(x)
# 	return x

from sys import stdin
input = stdin.readline

ballCount = int(input())
balls = list(map(int, input().split()))

# x coordinates represent the left bound, right bound is y
dp = [[-1 for _ in range(ballCount)] for _ in range(ballCount)]
res = max(balls)
for i in range(ballCount):
	dp[i][i] = balls[i]

for q in range(1,ballCount):
	for left, right in zip(range(ballCount), range(q, ballCount)):
		l1,r1 = left,left
		l2,r2 = right,right
		while r2>l1:
			#print([(l1,r1),(l2,r2)])
			#print((r2-1,l1+1))
			# #check l1,r1, l2,r2
			if dp[l1][r1] == dp[l2][r2] != -1:
				#print("true")
				# 0,0 3,1 => 1,0
				if r2-1>=l1+1:
					if dp[r2-1][l1+1]!=-1:
						dp[right][left] = dp[l1][r1]+dp[l2][r2]+dp[r2-1][l1+1]
				else: # edge case where one of original balls merges with everything else
					dp[right][left] = dp[l1][r1]+dp[l2][r2]
				
				res = max(res,dp[right][left])

			r2-=1
			if r2==l1:
				r2 = l2
				l1+=1
				if l1 == l2:
					break
		
		# if balls[right] == balls[left] and dp[right-1][left+1] != -1:
		# 	dp[right][left] = balls[right]+balls[left]+dp[right-1][left+1]
		# elif balls[left] == dp[right][left + 1] != -1:
		# 	dp[right][left] = balls[left]+dp[right][left + 1]
		# elif balls[right] == dp[right - 1][left] != -1:
		# 	dp[right][left] = balls[right]+dp[right-1][left]
		# else:
		# 	j = right-1
		# 	while j>left+1:
		# 		j-=1
		# 		if dp[j][left] == dp[right][j+1] != -1:
		# 			dp[right][left] = max(dp[right][left],dp[j][left]+dp[right][j+1])
		#res = max(res, dp[right][left])

#[print(row) for row in dp]
print(res) # answer