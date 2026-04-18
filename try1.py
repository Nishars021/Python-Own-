import numpy as np 
from scipy import sparse
# vector_row = np.array([1,2,3]) #create a vector as row
# vector_column = np.array([[1],[2],[3]])  #create a vector as column
# print(vector_row)
# print(vector_column)

#create a matrix
matrix = np.array([[0,0],[0,1],[3,0]])

#Create a compressed sparsh row matrix
matrix_sparse = sparse.csr_matrix(matrix)
print(matrix_sparse)