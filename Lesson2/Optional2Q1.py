#while loop - while there's next char in product i.e. like for loop
#take each char from product[]
#compare to see if I can find the char in the debris
# use find()
#if I can't find the char, return False
#else continue to the next char until I've finished all the characters in product
#if I get to the end of the loop return product



def fix_machine(debris, product):
    index = 0
    while index < len(product): # cycles through all characters in product
        #print index
        char = product[index]
        if debris.find(char) == -1:
            return "Give me something that's not useless next time."
        else: 
            index += 1 
    return product

## Can I write it in one line? 

### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'
