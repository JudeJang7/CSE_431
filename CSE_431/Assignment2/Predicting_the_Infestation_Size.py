kh = input().rstrip().split()

k = int(kh[0])
h = int(kh[1])

while (h > 0):
    # print(h)
    h -= k
    k *= 2
    # print(k)

k //= 2

if h < 0:
    print(h + k)
else:
    print(k)
