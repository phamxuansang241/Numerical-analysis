import pandas as pd
import numpy as np
import Diag_dom

matrixA = np.loadtxt("MatrixA.csv", delimiter=',')
matrixb = np.loadtxt("MatrixB.csv", delimiter=',')

def gauss_seidel(A, b, tolerance=1e-7, max_iterations=10000):
    print("Thực hiện lặp Gauss-Seidel với ma trận chéo trội hàng:\n")
  
    x = np.zeros_like(b, dtype=np.double)
    
    if Diag_dom.row_diag_dom(A) == False:
        print(" Ma trận A không chéo trội hàng.")
        return
    
    #Thực hiện lặp
    for k in range(max_iterations):
        
        x_old  = x.copy()
        
        #Duyệt các hàng của ma trận
        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i,:i], x[:i]) - np.dot(A[i,(i+1):], x_old[(i+1):])) / A[i ,i]
         
        print("Lần lặp thứ: ", k, ": ", x.transpose())
        
        #Điều kiện dừng
        if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tolerance:
            break

    print("\nNghiệm của hệ phương trình: ")
    for i in range(len(x)):
        print("x_{}: {}".format(i, x[i]))
    
    print("\nSai số: {}".format(np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf)))
    
x = gauss_seidel(matrixA, matrixb)
