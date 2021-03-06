# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input, 
# define a  procedure that returns True if the input is an identity matrix 
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements 
# on the principal/main diagonal are 1 and all the elements outside 
# the principal diagonal are 0. 
# (A square matrix is a matrix in which the number of rows 
# is equal to the number of columns)

def is_identity_matrix(matrix):
    
    # checks if square matrix. Returns false if not
    if not checkSize(matrix): 
        return False
    
    # check the diagonal is 1
    if not checkDiagonal(matrix):
        return False
    
    # check the rest of items in list are 0
    if not checkZero(matrix):
        return False
    
    # passed all tests
    return True    


def checkSize(matrix):
    numRows = len(matrix)
    for row in matrix: 
        if len(row) == numRows:
            return True
        else: 
            return False

def checkDiagonal(matrix): 
    i = 0
    for row in matrix: 
        # extracts each diagonal digit respective to row index
        # & tests for equality with 1
        if row[i] != 1: 
            return False
        else:
            i += 1
    return True
    
def checkZero(matrix):
    i = 0
    test = []
    for row in matrix: 
        
        #constructs new list removing diagonal digit
        test = row[:(i)] + row[(i+1):]
        for digit in test: 
            if digit != 0:
                return False
        i += 1 
    return True



# Test Cases:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix(matrix5)
#>>>False

matrix6 = [[1,0,0,0],  
           [0,1,0,2],  
           [0,0,1,0],  
           [0,0,0,1]]

print is_identity_matrix(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
#>>>False           

           