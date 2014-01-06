# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

'''
[
    e0[<keyword>,
        [<url>,url2]],
    e1[keyword2,
        [url, url2]]
    e2[keyword3,
        [url, url2]]
    e3[keyword4,
        [url, url2]]
]
'''


index = []

def add_to_index(index,keyword,url):
    if index:
        for e in index:
            # keyword already exists in index list
            if keyword in e:
                if url not in e[1]:
                    e[1].append(url)
            else:
                index.append([keyword,[url]])
    else: 
        index.append([keyword,[url]])
        
                        






add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]


