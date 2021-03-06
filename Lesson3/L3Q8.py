# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.


correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]


incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

               
def check_sudoku(square):
    numOfDig = len(square[0])
    sum = (numOfDig * (numOfDig + 1))/2
    if checkAllRow(square, numOfDig, sum):
        if checkAllCol(square, numOfDig, sum):
            return True
        else: 
            return False
    else:
        return False    
    
'''
            Pseudo Code
            series of checks to check Row:
            grab one list from Sudoku Square (contains 1 row)
            check length of each row
            check for duplicates? (check sum)
            use counter to check each digit
            
'''
def checkAllRow(square, numOfDig, sumAllDig):
    for row in square:  #row is a list containing digits
        if not checkRow(row, numOfDig, sumAllDig):
            return False
    return True 
        
def checkRow(rowList, numOfDig, sumAllDig):
    
        if len(rowList) != numOfDig: 
            return False
        
        # compares sum of digits in one row to sum should be found
        if sumAllDig != calcSumOneRow(rowList): 
            return False
        
        if not checkEachDigitOneRow(rowList, numOfDig):
            return False
        else: 
            return True
    
def calcSumOneRow(oneRow): 
    sum = 0   
    for digit in oneRow: 
        if not isinstance(digit, int):
            return False
        else:    
            sum += digit
    return sum
        
    
def checkEachDigitOneRow(oneRow, numOfDig):
    index = 1
    while index <= numOfDig:
        if index not in oneRow:
            return False
        index += 1
    return True

''' 
        Pseudo Code
        series of checks to check Column: 
        Trick accessing same col in each row 
        Create list with numbers gathered
        Run same check row code
        
'''


def checkAllCol(square, numOfDig, sumAllDig):
    index = 0
    while index < numOfDig:
        column = [] 
        for row in square:
            column.append(row[index])
        if checkRow(column, numOfDig, sumAllDig): 
            index += 1 
        else: 
            return False    
    return True         
        

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect)
#>>> False

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False
