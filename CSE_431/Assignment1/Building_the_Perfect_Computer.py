import math

def calculate(minimum, maximum):
    
    d = 0
    s = 0
    b = 0
    squares = []
    
    d = int(maximum / 12) - int(minimum / 12)
    if minimum % 12 == 0:
        d += 1
    
    s = math.floor(math.sqrt(maximum)) - math.ceil(math.sqrt(minimum))
    
    squares.append(math.ceil(math.sqrt(minimum)))
    i = 1
    while i < s + 1:
        squares.append(math.ceil(math.sqrt(minimum)) + i)
        i += 1
    
    for e in squares:
        if e * e % 12 == 0:
            b += 1
            
    if len(squares) >= 1:
        s += 1 
    if s <= 0:
        b = 0;
            
    return [d, s, b]
    
number = int(input())
i = 0
while i < number:
    range_of_cores = [int(x) for x in input().split()]
    calculations = calculate(range_of_cores[0], range_of_cores[1])
    
    j = 1
    for e in calculations:
        print(e, end = " ") 
        if j == len(calculations):
            print()
        j += 1
        
    i += 1
