t = int(input())

for i in range(t):
    
    ng = input().rstrip().split()
    n = int(ng[0])
    g = int(ng[1])
    
    answer = bin(n - g)
    
    counter = 0
    for i in range(2, len(answer)):
        if answer[i] == "1":
            counter += 1
    
    print(counter)
