t = int(input())

for i in range(t):
    
    minimum = 1
    maximum = 2000
    
    nk = input().split()
    number = int(nk[0])
    heat = int(nk[1])

    text = input().rstrip().split()

    buttons = []
    for button in text:
        buttons.append(int(button))
    buttons.sort()
    
    uniques = []

    for button in buttons:
        if button not in uniques:
            uniques.append(button)

    heats = [0] * heat

    for unique in uniques:
        if unique <= heat:
            heats[unique - 1] = unique

    for i in range(heats[0], len(heats)):
        if heats[i] == 0:
            heats[i] = heats[i-1]
            for j in range(heats[0], i):
                for unique in uniques:
                      if heats[i-j] + unique <= i + 1 and heats[i-j] + unique > heats[i]:
                        heats[i] = heats[i-j] + unique

    if (len(buttons) == 1 and buttons[0] == 1 and heat == minimum):
        print(heat)
    if (len(buttons) == 1 and buttons[0] == 1 and heat == maximum):
        print(heat)
    else:
        print(heats[-1])
