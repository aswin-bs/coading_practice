import numpy as np

def transpose(mat):
    return np.transpose(mat)

def mul(mat1 , mat2):
    return np.dot(mat1 , mat2)

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[7, 8], [9, 10]])


transposed_matrix1 = transpose(matrix1)


result_matrix = mul(transposed_matrix1, matrix2)

print(transposed_matrix1)
print(result_matrix)