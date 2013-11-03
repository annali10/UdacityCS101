def print_multiplication_table(n):
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            product = i * j
            print str(i) + " * " + str(j) + " = " + str(product)
            j += 1
        i += 1
    

print_multiplication_table(2)
print_multiplication_table(3)
        