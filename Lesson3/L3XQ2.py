# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.


'''
Pseudo code to solve: 
Calc length for size of puzzle/num of items in a row
Take first row
Compare to first column items (make sure identical)
Go to next row, take items from i=1 and compare to column 2 
from i=1
etc.
'''


def symmetric(puzzle):
    i = 0
    for row in puzzle: # one row in puzzle
        col = getCol(puzzle, i)
        newRow = row[i:]
        newCol = col[i:]
        if newRow != newCol:
            return False
        else:
            i += 1
    return True

def getCol(puzzle, i):
    col=[]
    for row in puzzle: 
        col.append(row[i])
    return col    


print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
               ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False