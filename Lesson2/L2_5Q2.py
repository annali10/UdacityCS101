# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct ouptuts yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 
from test.test_datetime import DAY

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
'''
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    daysInYear1 = convertToDays(year1, month1, day1)
    #print "daysInYear1: " + str(daysInYear1)
    daysInYear2 = convertToDays(year2, month2, day2)
    #print "daysInYear2: " + str(daysInYear1)
    #print "days = " + str(daysInYear2 - daysInYear1)
    if daysInYear1 < daysInYear2:
        return daysInYear2 - daysInYear1

def convertToDays(year, month, day):
    return year * 360 + month * 30 + day
'''
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    #programming defensively
    assert date2IsAfter(year1, month1, day1, year2, month2, day2)
    day = 0
    while date2IsAfter(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        day += 1
    return day

        

#year1, month1, day1 == first date
#year2, month2, day2 == second date
#I want second to be after first date

def date2IsAfter(year1, month1, day1, year2, month2, day2):
    if year2 > year1:
        return True
    if year2 == year1: 
        if month2 > month1: 
            return True
        if month2 == month1:
            return day2 > day1
    return False

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed", answer
        else:
            print "Test case passed!", answer

test()
    
