# Complete the monolithRotation function below.
# https://www.geeksforgeeks.org/rotate-matrix-elements/
def monolithRotation(matrix, rotations):
     
    t = l = 0
    r = len(matrix[0]) - 1
    b = len(matrix) - 1
  
    while l < r and  t < b: 

        prev = matrix[t][l+1] 
  
        for i in range(t, b+1): 
            curr = matrix[i][l] 
            matrix[i][l] = prev 
            prev = curr 
  
        l += 1
        
        for i in range (l, r+1): 
            curr = matrix[b][i] 
            matrix[b][i] = prev 
            prev = curr 
  
        b -= 1
        
        for i in range(b,  t-1, -1): 
            curr = matrix[i][r] 
            matrix[i][r] = prev 
            prev = curr 
  
        r -= 1
        
        for i in range(r, l-1, -1): 
            curr = matrix   [t][i] 
            matrix  [t][i] = prev 
            prev = curr 
  
        t += 1
  
    return matrix

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0]) # Number of rows

    n = int(mnr[1]) # Number of columns

    r = int(mnr[2]) # Number of rotations

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    i = 0
    while i < r:
        matrix = monolithRotation(matrix, r)
        i += 1
    
    for e in matrix:
        print(*e)
