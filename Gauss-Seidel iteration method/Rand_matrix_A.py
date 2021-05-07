import numpy as np
import pandas as pd


lower_bound = -200
upper_bound = 200
matrix_size = 100

 # Tạo ma trận A chéo trội hàng
def random_matrixA_matrixB(lower, upper, size):
    A = np.random.uniform(lower_bound, upper_bound, (size, size))
    A = A-np.diag(A)
    
    C = np.zeros((size, 1))
    for i in range(len(A)):
        C[i] = np.sum(np.absolute(A[i]))
    
    C = C + np.random.uniform(0, upper_bound, (size, 1))
    
    for i in range(len(A)):
        A[i,i] = A[i,i] + C[i]
        
    np.savetxt("MatrixA.csv", A, delimiter=',')
    
    B = np.random.uniform(lower_bound, upper_bound, (size, 1))    
    np.savetxt("MatrixB.csv", B, delimiter=',')
    
    return (A, B)
    
random_matrixA_matrixB(lower_bound, upper_bound, matrix_size)