'''
Flipkart Price Scrapping and Notify when
Price will decrease in our computer
Please install the packages 
'''
import requests
from bs4 import BeautifulSoup
import time
from notifypy import Notify

product_url = input("Enter the Product Url:")
price_list = []
class_text = "_30jeq3 _16Jk6d"

def get_price():
    getpage= requests.get(product_url)
    soup= BeautifulSoup(getpage.text, 'html.parser')
    price_tag = soup.find(class_ = class_text)
    price = (price_tag.get_text())
    price = float(price.replace(",", "").replace("₹", ""))
    price_list.append(price)
    return price

def price_decrease_check(price_list):
    if price_list[-1] < price_list[-2]:
        return True
    else:
        return False

count = 1

def notify():
    notification = Notify()
    notification.title = "Cool Title"
    notification.message = "Even cooler message."
    #notification.audio = "noti.wav"
    notification.send()

while True:
    current_price = get_price()
    if count > 1:
        flag = price_decrease_check(price_list)
        if flag:
            decrease = price_list[-1] - price_list[-2]
            message = f"The price has decrease please check the item. The price decrease by {decrease} rupees."
            notify()
    print(current_price)
    time.sleep(43000)
    count += 1
