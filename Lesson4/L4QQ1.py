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
    appendedUrl = False
    for keyword_listUrls in index:

        # keyword already exists in index list
        if keyword == keyword_listUrls[0]:
            if url not in keyword_listUrls[1]:
                appendedUrl = True
                keyword_listUrls[1].append(url)
    # if we didn't find the keyword in the list, add it.                

    if appendedUrl == False:
        index.append([keyword,[url]])
            
            



                        






add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]


