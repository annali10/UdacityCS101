def stamps(n):
    five = n /5
    two =  0
    one = 0
    if (n % 5) > 0:
        two = (n % 5) / 2
    if ((n % 5) % 2) > 0:
        one = 1
    return (five, two, one)  
    
print 3 / 2   
print stamps(2)
# 0, 1, 0
print stamps(3)
# 0, 1, 1
print stamps(29)
# 5, 2, 0
print stamps(8)
# 1, 1, 1
print stamps(0)
# 0, 0, 0
print stamps(5)
# 1, 0, 0
print stamps(7)
# 1, 1, 0