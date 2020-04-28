def calculate(lists):
    
    energy = 0
    
    for l in lists:
        i = 1
        for e in l:
            energy += i * e
            i += 1
            
    return energy
        

nk = input().rstrip().split()
n = int(nk[0]) # Number of instabilities
k = int(nk[1]) # Number of stabilizers
text = input().rstrip().split()
instabilities = []
lists = [[] for _ in range(k)]

for e in text:
    instabilities.append(int(e))
instabilities.sort(reverse = True)

i = 0
for e in instabilities:
  if i < k:
    lists[i].append(e)
    i += 1
  if i == k:
    i = 0

print(calculate(lists))
