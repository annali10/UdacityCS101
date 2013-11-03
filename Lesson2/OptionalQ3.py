def set_range(n1, n2, n3):
    biggest = max(n1,n2,n3)
    smallest = min(n1,n2,n3)
    return biggest - smallest

print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6