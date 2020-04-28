def calculate(case):
    
    points = case[0:2]
    moves = int(case[2])
    scores = []
    
    i = 0
    while i <= moves:
        scores.append((points[0] * (moves - i)) + (points[1] * i))
        i += 1
    
    return scores
    
number = int(input())
# number = 1 
i = 0
while i < number:
    case = [int(x) for x in input().split()]
    # case = [1, 2, 4]
    scores = calculate(case)
    
    scores = list(dict.fromkeys(scores))
    # get unique values from list
    
    scores.sort()
    
    # print(scores)
    
    for e in scores:
        if e == scores[-1]:
            print(e)
        else:
            print(e, end = " ")  
    i += 1
