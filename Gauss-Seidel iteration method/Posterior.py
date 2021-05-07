# Lặp đơn với đánh giá hậu tiên nghiệm

import pandas as pd
import numpy as np
import Find_norm

matrixA = np.loadtxt("Test/Test1_A.csv", delimiter=',')
matrixb = np.loadtxt("Test/Test1_b.csv", delimiter=',')

def iterate(A, b, tolerance=1e-10, max_iterations=10000):
    print("Lặp đơn với đánh giá hậu nghiệm:\n")
    
    x = np.zeros_like(b, dtype=np.float)
    # Chọn phương trình lặp: x = (I + A)x - b  (G = I + A, c = -b)
    G = np.eye(len(A)) + A
    c = -b
    if Find_norm.a_norm(G) is None:
        # Chọn lại phương trình lặp x = (I-A) + b  (G = I + A, c = b)
        G = np.eye(len(A)) - A
        c = b
        if Find_norm.a_norm(G) is None:
            print("Cần chọn một chuẩn khác.")
            return 
    
    # p là loại chuẩn của G
    p = Find_norm.a_norm(G)
    # q là chuẩn p của G
    q = np.linalg.norm(G, p)
    
    for k in range(max_iterations):
        x_old = x
        x = np.dot(G, x_old) + c
        
        if q*np.linalg.norm((x-x_old),p)/(1-q) < tolerance:
            print("Số lần lặp: {}\n".format(k))
            break

    print("Nghiệm của hệ phương trình: \n")

    for i in range(len(x)):
        print("x_{}: {}".format(i, x[i]))
    
iterate(matrixA, matrixb)