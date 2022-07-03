N, Q = map(int, input().split())
s = input()
query = [list(map(int, input().split())) for _ in range(Q)] # 1 x , 2 x

for q, x in query:
  if q == 2:
    print(s[x-1])
  else:
    s = s[-x:][::-1] + s[:-x]
