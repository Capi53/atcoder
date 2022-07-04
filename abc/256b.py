n = int(input())
A = list(map(int, input().split()))

MARGIN = 4
p = 0
for i in range(n):
  if sum(A[i:]) >= 4:
    p += 1
print(p)
