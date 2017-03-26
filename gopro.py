#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Chuang Yi, Wei'

import requests
from bs4 import BeautifulSoup

url ="http://www.csl-gp.com.tw/product-category/%E6%96%B0%E5%A2%9E%E5%95%86%E5%93%81%E5%88%86%E9%A1%9E%E5%90%8D%E7%A8%B1/"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

ul_soup=(soup.findAll('ul',{'class' : 'products'}))

produc_name = [];
price = [];

for product in ul_soup:
	produc_name = product.findAll('h3');
	price = product.findAll('span',{'class' : 'amount'})

name_len = len(produc_name);
amount_len = len(price);
i = 0;
j = 0;
while(i < name_len and j < amount_len):
	print ("{product_name:15} {price}".format(
		product_name = produc_name[i].text ,
		price = price[j].text
		)
	)
	i = i+1;
	j = j+1;

