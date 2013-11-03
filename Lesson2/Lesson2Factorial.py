
def factorial(n):
    total = 1
    i = 1
    while i <= n:
        # n! = n * (n - 1) * (n - 2) * ...3 * 2 * 1
        total = i * total
        i += 1
    return total    
        
print(factorial(0))
print(factorial(4))
print(factorial(10))
print(factorial(101))
print(factorial(5))
print(factorial(1))
print(factorial(3))


        
