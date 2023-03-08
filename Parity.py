
"""Given a any_size matrix matrix This program will
be able to check if there is a paradoy error
given that the key is n[0]Xn[0] 
by using the Matrix [0] and Matrix[:][0] as keys"""

# TODO fix column keys (array and lists)

import numpy as np


def parity_checker(matrix):
    row_index, column_index = 0, 0
    row_err = False
    col_err = False

    for i in matrix:  # for ech row in the matrix
        if ((np.sum(i[1:]) % 2) != i[0]).any():  # if the sum of the row (not including key) = key then valid
          row_err = True  
          row_err_index = row_index
          print(f'Row is invalid at index: {row_index}')  # TODO find for row that is invalid
        row_index += 1
    
    for i in matrix.T:  # this >T function transposes the matrix then does the same this as the first for loop
        if ((np.sum(i[1:]) % 2) != i[0]).any():
            col_err = True
            col_err_index = column_index
            
            print(f'Column is invalid at:{column_index} ')
        column_index += 1

    if(row_err and col_err):  # Ternary operator? 
      if matrix[row_err_index][col_err_index] == 1:
        matrix[row_err_index][col_err_index] = 0
      else:
        matrix[row_err_index][col_err_index] = 1
    
    print(matrix)

matrix = np.array([[1,0,1],[0,1,0],[1,0,1]])

parity_checker(matrix)
 # add tests
