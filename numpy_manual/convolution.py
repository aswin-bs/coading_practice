import numpy as np

def convolve(input , filter):

    input_h , input_w = input.shape
    filter_h , filter_w = filter.shape

    out_h , out_w = input_h - filter_h + 1 , input_w - filter_w + 1

    result = np.zeros((out_h , out_w))

    for i in range(out_h):
        for j in range(out_w):

            sub = input[i : i + filter_h , j : j + filter_w]
            result[i , j] = np.sum(sub*filter)   

    return result


matrix = np.array([[1, 2, 3, 0], 
                        [4, 5, 6, 1], 
                         [7, 8, 9, 0], 
                         [1, 1, 1, 0]])

filter = np.array([[1, 0], [0, -1]])


result_matrix = convolve(matrix, filter)

print(result_matrix)
