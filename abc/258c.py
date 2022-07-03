N, Q = map(int, input().split())
s = input()
query = [list(map(int, input().split())) for _ in range(Q)]

p = 0
for i in range(Q):
  q = query[i][0]
  x = query[i][1]

  if q == 1:
    p -= x
  else:
    print(s[(x - 1 + p) % N])
