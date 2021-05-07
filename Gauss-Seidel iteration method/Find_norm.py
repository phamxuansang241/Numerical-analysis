import pandas as pd
import numpy as np

#Tìm một chuẩn thích hợp
def a_norm(matrix):
    norm_list = []
    norm_list.append(np.linalg.norm(matrix, np.inf))
    norm_list.append(np.linalg.norm(matrix, 1))
    norm_list.append(np.linalg.norm(matrix, 2))
    if min(norm_list) > 1:
        return None
    else:
        for i in range(len(norm_list)):
            if norm_list[i] == min(norm_list):
                if i == 0:
                    return np.inf
                else:
                    return i