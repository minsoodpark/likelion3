#!/usr/bin/env python
# coding: utf-8

# In[56]:


import requests # from urllib.request import urlopen
from bs4 import BeautifulSoup # HTTP Response -> HTML

# import pandas as pd
# from datetime import datetime
# import time
# import re


# In[34]:


https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=을지면옥


# In[57]:


query = '을지면옥'
url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=" + query


# In[58]:


print(url)


# In[37]:


# web = urlopen(url)
# print(web)


# In[38]:


# web = requests.get(url).content
# print(web)


# In[59]:


web = requests.get(url).content
source = BeautifulSoup(web, 'html.parser')
# print(source) # source를 그대로 출력할 경우, 담고 있는 텍스트가 무척 많아서 버벅이게 될 수 있습니다.


# In[113]:


# 을지면옥 방문자 리뷰수
reviewcount = source.find_all('span', {'class': 'count'})[1].get_text()

review_list = []

review_list.append(reviewcount)

print(reviews_list)


# In[115]:


# # 을지면옥 평점 다른 방법
# float(rate.split('/')[0].strip())

# 을지면옥 평점 
rate = source.find_all('div', {'class': 'star_area'})[0].find('em').get_text()

rate_list = []

rate_list.append(rate)

print(rate_list)


# In[117]:


# 을지면옥 위치
location = source.find('span', {'class': 'addr'}).get_text()

location_list = []

location_list.append(location)

print(location_list)


# In[ ]:




