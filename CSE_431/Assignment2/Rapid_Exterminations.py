def find_min(jobs, completion):
    
    temp = jobs[0][0]
    minimum = jobs[0][1]
    for i in range(len(jobs)):
        time = jobs[i][0]
        hours = jobs[i][1]
        if time <= completion:
            if hours < minimum:
                minimum = hours
                temp = time
    
    return[temp, minimum]

n = int(input())
jobs = []

i = 0
while i < n:
    tl = input().rstrip().split()
    t = int(tl[0])
    l = int(tl[1])
    jobs.append([t,l])
    i += 1
    
jobs.sort()
time = jobs[0][0]
hours = jobs[0][1]
passed = hours
completion = time + hours
jobs.remove(jobs[0])

while len(jobs) >= 1:
    j = find_min(jobs, completion)
    # print(completion, j[1], j[0])
    completion += j[1]
    # print(completion)
    passed += completion - j[0]
    # print(passed)
    # passed += completion + j[1] - j[0]
    # passed += j[1]
    # print(j[0],j[1])
    # completion = completion + passed - j[0]
    jobs.remove(j)
    
answer = passed/n
print(int(answer))
