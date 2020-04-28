# https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
# Combination Function

import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

nm = input().rstrip().split()
n = int(nm[0])
m = int(nm[1])

pairs = []
for i in range(m):
    pair = input().rstrip().split()
    pairs.append([int(pair[0]),int(pair[1])])

# print(pairs)

unique = []
for pair in pairs:
  for p in pair:
    if p not in unique:
      unique.append(p)

l = []
for u in unique:
  li = []
  for pair in pairs:
    if u == pair[0]:
      li.append(pair[1])
    if u == pair[1]:
      li.append(pair[0])
  l.append(li)

# print(l)

maximum = 0
indx = 0
for i in range(len(l)):
  if len(l[i]) > maximum:
    maximum = len(l[i])
    indx = i

# print(maximum, indx)

answer = l[indx]
# print(answer)
answer.append(unique[indx])
# print(answer)

print(int(ncr(len(answer), 2)))
