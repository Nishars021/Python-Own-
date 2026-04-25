import numpy as np 
from scipy import sparse
# vector = np.array([1,2,3]) #create a vector as row
# print(vector[::-1]) #Reverse the row

# vector_column = np.array([[1],[2],[3]])  #create a vector as column
# print(vector_row)
# print(vector_column)

#create a matrix
# matrix = np.array([[0,0],[0,1],[3,0]])

# #Create a compressed sparsh row matrix

# matrix_sparse = sparse.csr_matrix(matrix)
# print(matrix_sparse)

# vector = np.zeros(shape=5)
# print(vector)

# matrix=np.full(shape=(2,5), fill_value=1)
# print(matrix)

matrix = np.array([[0,0],[1,0],[0,2]])
matrix_sparse = sparse.csr_matrix(matrix)
print(matrix_sparse)