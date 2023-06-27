#!/usr/bin/env python
# coding: utf-8

# In[137]:


import requests
from bs4 import BeautifulSoup

#Imdb Most Popular TV Shows
wb='https://www.imdb.com/chart/tvmeter'
url=requests.get(wb).text  
#requests.get()-> used to send an HTTP GET request to the specified website URL.

soup=BeautifulSoup(url,'html.parser')

show = soup.find('tbody',class_='lister-list').find_all('tr')
count=0
#We'll need to use a counter 

for i in show:
    count=count+1
    
    name = i.find('td',class_='titleColumn').a.text
    year = i.find('td',class_='titleColumn').span.text.strip('()')
       
    #It was found One Piece had no rating, so we'll use exception
    try:
        rate = i.find('td',class_='imdbRating').strong.text
    except:
        rate ='NA'
   
    #In order to get the proper rank, we'll use the count variable 
    if count<=9:
        rank = i.find('td',class_='titleColumn').get_text(strip=True).split(')')[1][0]
    elif count<100:
        rank = i.find('td',class_='titleColumn').get_text(strip=True).split(')')[1][0:2]
    else:
        rank = i.find('td',class_='titleColumn').get_text(strip=True).split(')')[1][0:3]
        
    print(rank, '-',name,'- ',year,' -',rate)

