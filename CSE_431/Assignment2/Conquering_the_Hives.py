n = int(input())

hive = 0
current = 0
new = 0
updated = 0

i = 0
j = 0
while i < n:
    
    nc = input().split()
    new = int(nc[0])
    cost = int(nc[1])
    
    updated = current + new;
    j += 1

    if updated < cost:
        current = 0
        hive = j

    if updated >= cost:
        current = current + new - cost
        
    i += 1
    # j += 1
        
print(hive)        
