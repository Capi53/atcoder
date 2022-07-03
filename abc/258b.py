n = int(input())
field = [list(map(int, list(input()))) for _ in range(n)]
ans = 0
ope = []
for i in range(-1, 2):
  for j in range(-1, 2):
    if i==j==0:
      continue
    ope.append([i,j])

for i in range(n):
  for j in range(n):
    x = j
    y = i
    for dx, dy in ope:
      tmp = 0
      for _ in range(n):
        tmp = tmp*10 + field[y][x]
        y += dy
        x += dx
        y %= n
        x %= n
      ans = max(ans, tmp)
print(ans)
