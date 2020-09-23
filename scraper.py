#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import smtplib
import time


URL = 'amazon url you want to track can keep the url till the product title'

headers = {"User-Agent":'Type : My User Agent on Google'}


def check_price():

    page = requests.get(URL, headers =headers)

    soup = BeautifulSoup(page.content,'lxml')

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[1:])
    

    print(converted_price)
    print(title.strip())
    if converted_price<75.0:
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('username', 'password')
    subject = 'Price fell down'
    body = f'check the amazon link{URL}'

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'from',
        'to',
        msg
    )
    print('EMAIL HAS BEEN SENT')
    server.quit()

while(True):
    check_price()
    # time.sleep()