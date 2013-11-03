def weekend(day):
    if day  == "Saturday": 
        return True
    if day == "Sunday": 
        return True
    return False
    
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False

