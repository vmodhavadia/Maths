from math import sqrt

def determinant(m):
    det = 0
    if len(m) == 4:
        det += m[0]*m[3] - m[1]*m[2]
    else:
        matrices = construct(m)
        dim = round(sqrt(len(m)))
        for i in range(dim):
            det += m[dim*i] * ((-1)**i) * determinant(matrices[i])
    return det

def construct(m): # returns list of new matrices to get the determinants of
    newms = []
    sqrl = round(sqrt(len(m)))
    for i in range(0, len(m) - sqrl + 1, sqrl):
            newms.append([m[j] for j in range(len(m)) if j % sqrl != 0 and (j-i > sqrl or j<i)])
    return newms

print(determinant([1, 2, 6, 0, 7, 2, 1, 0, 4, 0, 88, 0, 0, 15, 0, 2])) #should be -2192

    
    
