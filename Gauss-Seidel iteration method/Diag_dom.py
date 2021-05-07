import pandas as pd
import numpy as np

# Kiểm tra ma trận chéo trội hàng
def row_diag_dom(matrix):
    for i in range(len(matrix)):
        sum_row = np.sum(np.abs(matrix[i]))
        sum_row = sum_row - np.abs(matrix[i,i])
        if np.abs(matrix[i,i]) < sum_row:
            return False
    return True

# Kiểm tra ma trận chéo trội cột
def col_diag_dom(matrix):
    matrix = matrix.transpose()
    print(len(matrix))
    for i in range(len(matrix)):
        sum_row = np.sum(np.abs(matrix[i]))
        sum_row = sum_row - np.abs(matrix[i,i])
        if np.abs(matrix[i,i]) < sum_row:
            return False
    return True

