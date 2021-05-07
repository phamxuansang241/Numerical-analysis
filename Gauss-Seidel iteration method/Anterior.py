# Lặp đơn với đánh giá tiên nghiệm

import pandas as pd
import numpy as np
import Find_norm

matrixA = np.loadtxt("Test/Test1_A.csv", delimiter=',')
matrixb = np.loadtxt("Test/Test1_b.csv", delimiter=',')

def iterate(A, b, tolerance=1e-10):
    print("Lặp đơn với đánh giá tiên nghiệm:\n")
    
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
    
    x_old = x
    x = np.dot(G, x_old) + c
    # Tính số lần lặp 
    k = np.log(tolerance*(1-q)/np.linalg.norm((x-x_old), p))/np.log(q)
    k = int(np.ceil(k))
        
    print("Số lần lặp: {}\n".format(k))
    
    for i in range(k):
        x_old = x
        x = np.dot(G, x_old) + c
    
    print("Nghiệm của hệ phương trình: \n")

    for i in range(len(x)):
        print("x_{}: {}".format(i, x[i]))
    
iterate(matrixA, matrixb)