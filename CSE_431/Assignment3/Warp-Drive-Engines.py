def calculate(size, amount, frequencies, d):
    # print(size, amount, frequencies, d)
    steps = 0
    found = 0
    maximum = 0
    
    for frequency in frequencies:
        if frequency < size:
            if size % frequency == 0:
                found = True
                
                if frequency in d:
                    calculated = d[frequency]
                    if calculated > maximum:
                        maximum = calculated
                        
                if frequency not in d:
                    sizes = size // frequency
                    calculated = calculate(frequency, amount * sizes, frequencies, d)
                    if calculated > maximum:
                        maximum = calculated
                        
    if found == True:
        maximum += amount
        steps = maximum
        d[size] = maximum
        
    return steps

t = int(input())

for i in range(t):
    
    sk = input().split()
    size = int(sk[0])
    number = int(sk[1])
    text = input().rstrip().split()
    
    frequencies = []
    for frequency in text:
        frequencies.append(int(frequency))
        
    frequencies = list(dict.fromkeys(frequencies))
    frequencies.sort()
    
    d = {}
    
    print(calculate(size, 1, frequencies, d))
