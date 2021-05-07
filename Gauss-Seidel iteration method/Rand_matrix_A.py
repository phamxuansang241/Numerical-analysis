import numpy as np
import pandas as pd


lower_bound = -10
upper_bound = 10
matrix_size = 3

 # Tạo ma trận A chéo trội hàng
def random_matrixA_matrixb(lower, upper, size):
    A = np.random.uniform(lower_bound, upper_bound, (size, size))
    A = A-np.diag(A)
    
    C = np.zeros((size, 1))
    for i in range(len(A)):
        C[i] = np.sum(np.absolute(A[i]))
    
    C = C + np.random.uniform(0, upper_bound, (size, 1))
    
    for i in range(len(A)):
        A[i,i] = A[i,i] + C[i]
        
    np.savetxt("Test/Test0_A.csv", A, delimiter=',')
    
    b = np.random.uniform(lower_bound, upper_bound, (size, 1))    
    np.savetxt("Test/Test0_b.csv", b, delimiter=',')
    
    return (A, b)
    
random_matrixA_matrixb(lower_bound, upper_bound, matrix_size)