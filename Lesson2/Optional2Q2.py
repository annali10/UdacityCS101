
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel).

'''Pseudo code
calculate difference between year2 - year 1; month2 - month1; day2 - day1
multiply difference of year with 365.25
take into account the difference in months from the beginning of year to date given
i.e. if Dec 1998 and Jan 2004 - take into account most of 1998 won't be there
month1 with 30 unless it's Jan, Mar, May, July, Aug, Oct or Dec, or Feb which is 28 or 
29 if it's a leap year - calculate leap year if divisible by 4 but not 100 unless also
divisible by 400
Add the difference in days
'''

'''
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    yearsInDays = (year2 - year1) * 365.25
    monthInDays = calcMonth(month2, month1,)
    daysDiff = (day2 - day1)
    print yearsInDays + monthInDays + daysDiff
    return yearsInDays + monthInDays + daysDiff


def calcMonth(m1, m2):
    if (m2 - m1) == 1: #January
        return 31 
    elif (m2 - m1) == 2: #February
        return 31 + 28
    elif (m2 - m1) == 3: #March
        return 31 + 28 + 31
    elif (m2 - m1) == 4: #April
        return 31 * 2 + 28 + 30
    elif (m2 - m1) == 5: #May
        return 31 * 3 + 28 + 30
    elif (m2 - m1) == 6: #June
        return 31 * 3 + 28 + 30 * 2
    elif (m2 - m1) == 7: #July
        return 31 * 4 + 28 + 30 * 2
    elif (m2 - m1) == 8: #August
        return 31 * 5 + 28 + 30 * 2
    elif (m2 - m1) == 9: # September
        return 31 * 5 + 28 + 30 * 3
    elif (m2 - m1) == 10: #October
        return 31 * 6 + 28 + 30 * 3
    elif (m2 - m1) == 11: # November
        return 31 * 6 + 28 + 30  * 4
    else: 
        return 0
        
**** 
#new try

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    daysInYear1 = (year1 + month1 /12) * 365.25  + day1
    print "days in year 1" + str(daysInYear1)
    daysInYear2 = (year2 + month2 /12) * 365.25 + day2
    print "days Year 2" + str(daysInYear2)
    print daysInYear2 - daysInYear1
    return daysInYear2 - daysInYear1
'''
    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    return ifLeapYear(year1)
    
daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def ifLeapYear(year):
    if year % 4 == 0:
        if year % 100 != 0: 
            if year % 400 == 0:
                return True
    else:
        return False

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
