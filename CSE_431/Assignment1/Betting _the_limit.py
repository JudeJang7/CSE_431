def calculate(a, b):
    m = min(b)
    c = []
    for e in b:
        f = e - m
        if f > 0:
            c.append(f)
    return c
        
amount = int(input())
p = [int(x) for x in input().split()]

first = True
if first == True:
    first = False;
    print(amount)
    
while amount >= 2:
    c = calculate(amount, p)
    amount = len(c)
    if amount > 0:
        print(amount)
        p = c
