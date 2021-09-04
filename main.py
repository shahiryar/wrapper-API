import scholarly
import json
from scholarly import scholarly, ProxyGenerator

def handler(event):
    fn = event['operation']
    string = 'no results found'
    if (fn == 'ping'):
        return 'lambda function pinged successfully'
    
    if(fn == 'search_author'):
            ##setting proxy
        pg = ProxyGenerator()
        pg.FreeProxies()
        scholarly.use_proxy(pg)

        search_query = scholarly.search_author(event['queryStringParameters']['payload'])
        string = str(next(search_query)['url_picture'])
    else:
        string = find_pubs_for(event['payload'], event['fill'])
    
    #responseObj = {}
    #responseObj['statuscode'] = 200
    #responseObj['header'] = {}
    #responseObj['header']['Content-Type'] = 'applicaiton/json'
    #responseObj['body'] = string
    
    #return responseObj
    return string

def find_pubs_for(name, fill = "False"):
    #use proxy
    pg = ProxyGenerator()
    pg.FreeProxies()
    scholarly.use_proxy(pg)
    
    #getting author object from scholarly
    search_query = scholarly.search_author(name)
    author = next(search_query)
    filledAut = scholarly.fill(author, sections= ['publications'])
    pubs = filledAut['publications']
    #getting publications for found author
    if(fill=="True"):
        #filling in the publications
        fPubs =[]
        for pub in pubs:
            fPubs.append(str(scholarly.fill(pub)))
            print(pub)
            print('\n')
            #####remove this line
            break
            #####
        return json.dumps(fPubs)
    return json.dumps(pubs)

