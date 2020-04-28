nmk = input().rstrip().split()
n = int(nmk[0])
m = int(nmk[1])
k = int(nmk[2])

l1 = []
for i in range(m):
  edge = input().rstrip().split()
  e1 = int(edge[0])
  e2 = int(edge[1])
  l1.append((e1,e2))

l2 = []
for i in range(n-1):
  # print(i)
  for j in range(n):
    # print(j)
    if j > i:
      l2.append((i, j))

# print(l2)

n2 = n
m2 = int(n * (n-1) / 2 - m)
k2 = n - k

print(n2, m2, k2)
for e in l2:
  if e not in l1:
    print(e[0], e[1])
