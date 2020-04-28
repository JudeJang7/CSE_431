[N, P] = map(int, input().split(" "))              # N: number of colors/people; P: id of current person
possible_colors = input().split(" ")               # All possible colors
view = [c for c in input().split(" ") if c != ""]  # Hat colors this person sees (if there's only one player, we may see nothing!)

# ... code up your strategy here & print out your guess ...

indx = 0
for i in range(N - 1):
  for j in range(len(possible_colors)):
    if view[i] == possible_colors[j]:
      indx += j
P -= indx
indx = P % N
print(possible_colors[indx])
