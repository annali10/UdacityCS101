'''
Created on Sep 17, 2013

@author: annali
'''
def method(n):
    i = 1
    while True:
        i = i * 2
        n = n + 1
        print n, i
        if i > n:
            break
    print '***'

            
method(3)
method(9)
method(1000)
method(1)
method(50494)


def find_last(search, target):
    index = search.find(target)
    while index != -1:
        new_index = search.find(target, index + 1)
        if new_index != -1: 
            index = new_index
        else: 
            break
        #print index
    return index


print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
#>>> 9

print find_last("", "3")
#>>> -1

print find_last("", "")
#>>> 0



