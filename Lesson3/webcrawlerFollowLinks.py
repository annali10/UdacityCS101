
def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links    


def get_next_target(webpage):
    start_link = webpage.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote= webpage.find('"', start_link)
    end_quote = webpage.find('"', start_quote + 1)
    url = webpage[start_quote + 1:end_quote]
    return url, end_quote    
