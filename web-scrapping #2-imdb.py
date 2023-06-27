#!/usr/bin/env python
# coding: utf-8

# In[11]:


import requests
from bs4 import BeautifulSoup

#Imdb Most Popular TV Shows
wb='https://www.imdb.com/chart/tvmeter'
url=requests.get(wb).text  
#requests.get()-> used to send an HTTP GET request to the specified website URL.

soup=BeautifulSoup(url,'html.parser')


# In[12]:


show = soup.find('tbody',class_='lister-list').find_all('tr')


#  

# NAME column

# In[43]:


for i in show:
    name = i.find('td',class_='titleColumn').text
    print("NAME: "+name)
    break


# In[49]:


for i in show:
    name = i.find('td',class_='titleColumn').a.text
    print("NAME: "+name)
    break
#a is used to access the <a> element within the found HTML element. 


#   

# Year column

# In[50]:


for i in show:
    year = i.find('td',class_='titleColumn').text
    print("YEAR:",year)
    break


# In[51]:


for i in show:
    year = i.find('td',class_='titleColumn').span.text
    print("YEAR:",year)
    break
#.span is used to access the <span> element within the found HTML element. The span tag often contains the year information.


# In[53]:


for i in show:
    year = i.find('td',class_='titleColumn').span.text.strip('()')
    print("YEAR:",year)
    break
#Strip function to used to remove the Parentheses 


#  

# Rate Column

# In[62]:


for i in show:
    rate = i.find('td',class_='imdbRating').strong.text
    print("RATE:",rate)


# In[64]:


#It was found One Piece had no rating, so we'll use exception
for i in show:    
    try:
        rate = i.find('td',class_='imdbRating').strong.text
    except:
        rate ='NA'
    print("RATE:",rate)


#  

# Rank column

# In[72]:


for i in show:
    rank = i.find('td',class_='titleColumn').get_text(strip=True)
    print(rank)
    break


# In[80]:


#We need the rank 1 from the above output
for i in show:
    rank = i.find('td',class_='titleColumn').get_text(strip=True).split(')')
    print(rank)
    break


# In[82]:


#We'll need to focus on the second item and the first number from it
for i in show:
    rank = i.find('td',class_='titleColumn').get_text(strip=True).split(')')[1][0]
    print(rank)


# In[83]:


#However, after 9 the number are in double digits, and also 100 is of 3 digits
#We'll need to use a count then


#  

# FINAL loop

# In[84]:


count=0
for i in show:

    #We'll need to use a counter 
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

