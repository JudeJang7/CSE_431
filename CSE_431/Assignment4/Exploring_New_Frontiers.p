def calculate(candidates, requiredSkills):
    minimum = len(candidates)
    for i in range(len(candidates)):
        candidate = candidates[i]
        newRequiredSkills = requiredSkills.difference(candidate)
        if len(newRequiredSkills) == len(requiredSkills):
            continue
        if len(newRequiredSkills) == 0:
            return 1
        newCandidates = []
        for j in range(len(candidates)):
            if j != i:
                temp = len(newRequiredSkills.difference(candidates[j]))
                if temp != len(newRequiredSkills):
                    newCandidates.append(candidates[j])
        calculated = calculate(newCandidates, newRequiredSkills) + 1
        if calculated < minimum:
            minimum = calculated
    return minimum

def remove(candidates):
    l = []
    for i in range(len(candidates)):
        for j in range(len(candidates)):
            if i != j:
                if len(candidates[i]) > len(candidates[j]):
                    temp = len(candidates[i].difference(candidates[j]))
                    if temp == len(candidates[i]) - len(candidates[j]):
                        if j not in l:
                            l.append(j)
    l.sort(reverse=True)
    for i in l:
        candidates.pop(i)
        

nk = input().split()
n = int(nk[0])
k = int(nk[1])
skills = set(input().split())

candidates = []
for i in range(n):
    amount = int(input())
    candidates.append(set(input().split()))
remove(candidates)

print(calculate(candidates, skills))
