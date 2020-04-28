# https://stackoverflow.com/questions/10797819/finding-the-mode-of-a-list
from statistics import mode 

n = input()
ids = []

i = 0
while i < int(n):
    a = input()
    ids.append(int(a))
    i += 1
  
print(mode(ids))
