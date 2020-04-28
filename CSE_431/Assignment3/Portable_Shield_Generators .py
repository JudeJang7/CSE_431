n = input()
text = input().rstrip().split()
strengths = []

for strength in text:
    strengths.append(int(strength))

include = strengths[0]
exclude = 0
answer = 0
 
i = 1
while i < len(strengths):
    
    previous = include
    new = exclude + strengths[i]
    
    if exclude > new:
        include = include
    if include < new:
        include = new
        
    exclude = previous
    
    i += 1

if exclude > include:
    answer = exclude    
if exclude <= include:
    answer = include
    
print(answer)	
