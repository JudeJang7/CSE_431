nk = input().rstrip().split()
n = int(nk[0])
k = int(nk[1])
text = input()

l = []
encoded = []
decoded = ""

for i in range(n):
    l.append(int(text[i]))
    encoded.append(int(text[i]))
    
decoded += (str(l[0]))

for i in range(1, n):
    
    if i < k:
        temp = encoded[i - 1]
    
    if i >= k:
        temp = encoded[i - 1] + l[i - k]
        
    if encoded[i] % 2 == 0:
        if temp % 2 == 0:
            l[i] = 0
        if temp % 2 == 1:
            l[i] = 1
        
    if encoded[i] % 2 == 1:
        if temp % 2 == 0:
            l[i] = 1
        if temp % 2 == 1:
            l[i] = 0

    decoded += str(l[i])

print(decoded)
