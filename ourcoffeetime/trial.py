import requests,json
import random
# enter your api key here


def findList(location, place):
    api_key = 'NbEE2licArPR88IEjsCsbm6YhSF4_elK2Wu-StTxq9Ee-UG-C1gxyTiZv7s_g1nxDnSlFxLpeEpfiFX5FTVnwdCFrgH7fwNHP9PG55O5c7Osijhk_zC95ob2Zb8FYXYx'
    headers = {'Authorization': 'Bearer {}'.format(api_key)}
    search_api_url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term': place, 
            'location': location,
            'limit': 50}
    response = requests.get(search_api_url, headers=headers, params=params, timeout=5)
    results = response.json() 
    m = results['businesses'][0]
    for k in results['businesses']:
        if k['rating'] >m['rating'] and k['review_count']>3:
            m=k
    cat = [ i['title'] for i in m['categories']]
    try:
        ldict = {'name': m['name'], 'imageurl':m['image_url'], 'url':m['url'], 'address': (m['location']['display_address'][0]+", "+m['location']['display_address'][1]), 'phone':m['display_phone'], 'rating':m['rating'], 'price':m['price'], 'type' :cat}    
    except KeyError:
        ldict = {'name': m['name'], 'imageurl':m['image_url'], 'url':m['url'], 'address': (m['location']['display_address'][0]+", "+m['location']['display_address'][1]), 'phone':m['display_phone'], 'rating':m['rating'], 'type' :cat}    
    return ldict

# for i in ['name', 'imageurl', 'url', 'address', 'phone', 'rating', 'price', 'types']:
#     print("'" + i + "'" + " : "+ i+",")
def randomize(location, place):
    api_key = 'NbEE2licArPR88IEjsCsbm6YhSF4_elK2Wu-StTxq9Ee-UG-C1gxyTiZv7s_g1nxDnSlFxLpeEpfiFX5FTVnwdCFrgH7fwNHP9PG55O5c7Osijhk_zC95ob2Zb8FYXYx'
    headers = {'Authorization': 'Bearer {}'.format(api_key)}
    search_api_url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term': place, 
            'location': location,
            'limit': 50}
    response = requests.get(search_api_url, headers=headers, params=params, timeout=5)
    results = response.json() 
    length = len(results['businesses'])
    randomstore = random.randint(0, length-1)
    m = results['businesses'][randomstore]
    cat = [ i['title'] for i in m['categories']]
    try:
        ldict = {'name': m['name'], 'imageurl':m['image_url'], 'url':m['url'], 'address': (m['location']['display_address'][0]+", "+m['location']['display_address'][1]), 'phone':m['display_phone'], 'rating':m['rating'], 'price':m['price'], 'type' :cat}    
    except KeyError:
        ldict = {'name': m['name'], 'imageurl':m['image_url'], 'url':m['url'], 'address': (m['location']['display_address'][0]+", "+m['location']['display_address'][1]), 'phone':m['display_phone'], 'rating':m['rating'], 'type' :cat}    
    return ldict

    