import requests
import bs4
import time
import schedule
import os


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

# send_url = os.environ['SEND_URL']

print("Program starts...")

def check(title, url):
    r = requests.get(url, headers=HEADERS)
    soup = bs4.BeautifulSoup(r.content, features="lxml")
    # this part gets the price in dollars from amazon.com store
    try:
        price = float(soup.find(id='priceblock_ourprice').get_text().replace('$', '').replace(',', '').strip())
        
    except Exception as err:
        price = ''
        print("Error info:", err)
 
    msg = f"price: {price}$"
    print("--------------------> ",msg)
    requests.get(send_url + title + ":\n"+msg +"\n"+ url)


check("500G SSD", "https://www.amazon.com/dp/B08S8J19XJ?tag=camelproducts-20&linkCode=ogi&th=1&psc=1&language=en_US")