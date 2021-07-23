import requests
import bs4
import time
import schedule
import os


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

send_url = os.environ['SEND_URL']

print("Program starts...")

def check(title, url):
    r = requests.get(url, headers=HEADERS)
    time.sleep(5)
    soup = bs4.BeautifulSoup(r.content, features="lxml")
    # this part gets the price in dollars from amazon.com store
    try:
        price = float(soup.find(id='priceblock_ourprice').get_text().replace('$', '').replace(',', '').strip())
        
    except Exception as err:
        price = ''
        print("Error info:", err)

    # price1 = soup.find(id='priceblock_ourprice').get_text().replace('$', '').replace(',', '').strip()
    # price2 = soup.find(id='priceblock_ourprice').get_text().replace('$', '').replace(',', '')
    # price3 = soup.find(id='priceblock_ourprice').get_text().replace('$', '')
    # price4 = soup.find(id='priceblock_ourprice').get_text()
    # price5 = soup.find(id='priceblock_ourprice')    
    msg = f"price: {price}$"
    print("--------------------> ",msg)
    # requests.get(send_url + title + ":\n"+msg +"\n"+ url)
    # requests.get(send_url + price)
    # requests.get(send_url + price1)
    # requests.get(send_url + price2)
    # requests.get(send_url + price3)
    # requests.get(send_url + price4)
    # requests.get(send_url + price5)
    requests.get(send_url + r.)



check("500G SSD", "https://www.amazon.com/dp/B08S8J19XJ?tag=camelproducts-20&linkCode=ogi&th=1&psc=1&language=en_US")
# schedule.every().day.at("07:00").do(check, "500G SSD", "https://www.amazon.com/dp/B08S8J19XJ?tag=camelproducts-20&linkCode=ogi&th=1&psc=1&language=en_US")
# schedule.every().day.at("07:00").do(check, "Sunglasses", "https://www.amazon.com/Ray-Ban-Polarized-Rectangular-Sunglasses-Gradient/dp/B00NH9DWXI/ref=sr_1_3?dchild=1&keywords=RB4179&qid=1626975182&sr=8-3")

# while True:
    # schedule.run_pending()
    # time.sleep(10)