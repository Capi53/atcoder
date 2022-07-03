n, x = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
 
stageN = ab[0][0] + ab[0][1]
ans = stageN + ab[0][1]*(x-1)
 
for i in range(1, min(n,x)):
  stageN += ab[i][0] + ab[i][1]
  tmp = stageN + ab[i][1]*(x-(i+1))
  ans = min(ans, tmp)
print(ans)
