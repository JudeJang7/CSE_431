kn = input().rstrip().split()

k = int(kn[0]) # Number of reports coming in
n = int(kn[1]) # Number that Millenium can deal with

infestations = []

i = 0
while i < k:
    infestations.append(int(input()))
    i += 1

infestations.sort(reverse=True)

j = 0
while j < n:
    print(infestations[j])
    j += 1
