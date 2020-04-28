nm = input().rstrip().split()
n = int(nm[0])
m = int(nm[1])

l1 = []
for i in range(m):
  edge = input().rstrip().split()
  e1 = int(edge[0])
  e2 = int(edge[1])
  l1.append((e1,e2))

t = int(input())

l2 = []
for i in range(t):
  line = input().rstrip().split()
  l = []
  for e in line:
    l.append(int(e))
  l2.append(l)

# print(l1)
# print(l2)

for e in l2:
  flag = "YES"

  length = len(e)
  s = set(e)

  # print(length, len(s))

  for i in range(len(e)-1):

    edge = (e[i], e[i+1])
    r_edge = (e[i+1], e[i])
    final = (e[0], e[-1])
    r_final = (e[-1], e[0])

    if length != len(s):
      flag = "NO"

    if edge not in l1:
      if r_edge not in l1:
        flag = "NO"

    if final not in l1:
      if r_final not in l1:
        flag = "NO"

      
  print(flag)
