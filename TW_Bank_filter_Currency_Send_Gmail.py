# -*- coding: UTF-8 -*-
"""
    Author: 'Chuang Yi, Wei'
"""
__author__ = 'Chuang Yi, Wei'

import sys
import requests
from bs4 import BeautifulSoup
import time
import smtplib

class TW_BANK():
    chinese_table = {}
    online_currency = {}
    url = "http://rate.bot.com.tw/xrt?Lang=zh-TW"   
   
    def setCurrency(self, currency):        
        self.online_currency[currency] = []
        
    def getRate(self, soup):
        tr_tags=(soup.findAll('tr'))
        for tr_tag in tr_tags:
            currencies = tr_tag.findAll('div',{'class' : 'visible-phone print_hide'})
            for currency in currencies:
                #split Chinese and English string
                pattern = (currency.text.strip().split(" ")[1])
                #skip brackets in the string
                pattern = pattern[1:-1]
                self.chinese_table[pattern] = currency.text.strip().split(" ")[0]
                if pattern in self.online_currency:
                    td_tag = tr_tag.findAll('td',{'class' : 'rate-content-cash text-right print_hide'})
                    for rate_row in td_tag:
                        self.online_currency[pattern].append(rate_row.text.strip())
    
    def start(self):
        session = requests.Session()
        try:
            while True:
                print ("================ Monitor Start ====================")
                print (time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))) 
                res = session.get(self.url)
                soup = BeautifulSoup(res.text, 'html.parser')
                self.getRate(soup)
                #show price on console and check the target price
                for key, value in self.online_currency.items():
                    print (((self.chinese_table[key]) + key + " in Taiwan Bank is " + value[1]))
                    if(currency == key and float(value[1]) <= targetPrice):
                        print ("taget price reach , send mail and exit the program!") 
                        self.send_gamil(emai_conn, to_mail_list);                        
                        return
                time.sleep(5)# query every 5 secs
        except:
            print ("error during monitor")
        finally:
            print ("close session")
            session.close()

    def login_gmail(self, emai_conn, from_email, password):
        try:
            emai_conn.ehlo()
            emai_conn.starttls()
            emai_conn.login(from_email, password)
        except:
            print ("error during login gmail")

    def send_gamil(self, emai_conn, to_mail_list):
        try:
            title = "[TW Bank] Your taget price is reached"
            message_content = '[TW Bank] Your taget price is reached'
            message = 'Subject: {title}\n{message_content}'.format(
                    title = title,
                    message_content = message_content
                    )  
            emai_conn.sendmail(from_email, to_mail_list, message)
            emai_conn.quit()
        except:
            print ("error during send gmail")


keys = """
TW BANK Currency :
美金(USD),港幣(HKD),英鎊(GBP),澳幣(AUD)
加拿大幣(CAD),新加坡幣(SGD),瑞士法郎(CHF),日圓(JPY)
南非幣(ZAR),瑞典幣(SEK),紐元(NZD),泰幣(THB)
菲國比索(PHP),印尼幣(IDR),歐元(EUR),韓元(KRW)
越南盾(VND),馬來幣(MYR),人民幣(CNY)
"""
print (keys)
currency_obj = TW_BANK()

#input from user
currency = input("please chose the currency you want \n(EX:JPY)\n")
email = input("please enter the email you want to send: \n(EX:xxx@gmail.com)\n")
targetPrice = input("please enter the target price : \n(EX:0.5)\n")

to_mail_list = [email]
targetPrice = float(targetPrice)

#set currency
currency = currency.upper()
currency_obj.setCurrency(currency)

#login gmail
host = "smtp.gmail.com"
port = 587 
emai_conn = smtplib.SMTP(host, port)
from_email = "999taiwan888@gmail.com"
password = "tigerisfast"
currency_obj.login_gmail(emai_conn, from_email, password)

#start monitor
currency_obj.start()

print ("Exit Program")


