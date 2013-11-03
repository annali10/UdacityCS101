

def print_abacus(value):
    strValue = str(value)
    placeholder = "0000000000"
    placeholder = placeholder[:10 - len(strValue)] + strValue
    j = 0
    while j <= 9:
        print drawOneLine(placeholder[j])
        j += 1
    

# n is a string that represents the value to be drawn in the abacus       
def drawOneLine(n):
    abacusString = "|00000*****|"
    gap = "   "
    return abacusString[:(indexString(n))] + gap + abacusString[indexString(n):]
        
# n is a string that represents the value to be drawn in the abacus       
def indexString(n):  
    num = int(n)
    return -num - 1

print_abacus(1234)
print "***"
print_abacus(0)