'''
Created on Sep 16, 2013

@author: annali
'''
#Q1 udacify
def udacify(s):
    return "U" + s

#Q2 multiple choice, which is the same procedure?
def test(n):
    return n


def proc(a,b):
    if test(a):
        return b
    return a

print(proc(6,3))

#Q3 Gold star - function to find median
def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(n1, n2, n3):
    biggestN = biggest(n1, n2, n3)
    if n1 == biggestN:
        return bigger(n2, n3)
    else:
        if n2 > n3:
            return bigger(n1, n3)
        else:
            return bigger(n1, n2)
        

print(median(1,2,3))
#>>> 2
print(median(9,3,6))
#>>> 6
print(median(7,8,7))
#>>> 7

#Q4 Blastoff
def countdown(n):
    i = n
    while i > 0:
        print(i)
        i -= 1
    print("Blastoff!")
         
countdown(3)