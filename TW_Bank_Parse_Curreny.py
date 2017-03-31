# -*- coding: UTF-8 -*-
"""
    Author: 'Chuang Yi, Wei'
"""
__author__ = 'Chuang Yi, Wei'

import sys
import requests
from bs4 import BeautifulSoup
import time

def addFilterRule(currency):
    online_currency[currency] = []
    
def parsingRate(soup):
    tr_tags=(soup.findAll('tr'))
    for tr_tag in tr_tags:
        currencies = tr_tag.findAll('div',{'class' : 'visible-phone print_hide'})
        for currency in currencies:
            #split Chinese and English string
            pattern = (currency.text.strip().split(" ")[1])
            #remove brackets in the string
            pattern = pattern[1:-1]
            chinese_table[pattern] = currency.text.strip().split(" ")[0]
            if pattern in online_currency:
                td_tag = tr_tag.findAll('td',{'class' : 'rate-content-cash text-right print_hide'})
                for rate_row in td_tag:
                    online_currency[pattern].append(rate_row.text.strip())
'''
ex:
(USD),(HKD),(GBP),(AUD)
(CAD),(SGD),(CHF),(JPY)
(ZAR),(SEK),(NZD),(THB)
(PHP),(IDR),(EUR),(KRW)
(VND),(MYR),(CNY)
'''   
chinese_table = {}
online_currency = {}
 
addFilterRule('JPY')
addFilterRule('NZD')
addFilterRule('USD')

url = "http://rate.bot.com.tw/xrt?Lang=zh-TW"
session = requests.Session()

while True:
    print ("================================================")
    print (time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))) 
    res = session.get("http://rate.bot.com.tw/xrt?Lang=zh-TW")
    soup = BeautifulSoup(res.text, 'html.parser')
    parsingRate(soup)
    #show price on console and check the target price
    for key, value in online_currency.items():
        print (((chinese_table[key]) + key + " in Taiwan Bank is " + value[1]))
   
    time.sleep(5)# query every 5 secs
