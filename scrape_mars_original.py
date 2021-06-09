#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[ ]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


url = 'https://redplanetscience.com/'
browser.visit(url)


# # for none DYNAMIC CONTENT
# response = requests.get(url)
# soup = bs(response.text, 'lxml') #html.parser
# print(soup.prettify())

# In[ ]:


html = browser.html
soup = bs(html, 'lxml')


# In[ ]:


print(soup.prettify())


# In[ ]:


results = soup.find_all('div', class_='list_text')


# # Error handling
# for result in results:
#     try:
#         # Identify and return title of listing
#         title = result.find(class_='content_title').text
#         # Identify and return price of listing
#         teaser = result.find(class_='article_teaser_body').text
#         # Identify and return link to listing
#         #link = result.a['href']
# 
#         # Print results only if title, price, and link are available
#         if (title and teaser):
#             print('-------------')
#             print(title)
#             print(teaser)
#     except AttributeError as e:
#         print(e)

# In[ ]:


for result in results:
        # Identify and return title of listing
        title = result.find(class_='content_title').text
        # Identify and return teaser of listing
        teaser = result.find(class_='article_teaser_body').text

        # Print results only if title, price, and link are available
        print('-------------')
        print(title)
        print(teaser)


# In[ ]:


browser.quit()


# In[ ]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


url2 = 'https://spaceimages-mars.com/'
browser.visit(url2)
html = browser.html
soup2 = bs(html, 'lxml')


# In[ ]:


print(soup2.prettify())


# In[ ]:


featured_image = soup2.find(class_='showimg fancybox-thumbs')
featured_image


# In[ ]:


featured_image_url = format(featured_image.get('href'))
featured_image_url_final = url2 + featured_image_url
featured_image_url_final


# In[ ]:


browser.quit()


# In[ ]:


url3 = 'https://galaxyfacts-mars.com/'
tables = pd.read_html(url3)
tables


# In[ ]:


planet_facts_df = tables[0]
planet_facts_df.set_index(0,inplace= True)
planet_facts_df


mars_facts_table = planet_facts_df.to_html


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[18]:


url4 = 'https://marshemispheres.com/'
browser.visit(url4)
html = browser.html
soup4 = bs(html, 'lxml')


# In[4]:


print(soup4.prettify())


# In[ ]:


sidebar2 = soup4.findAll('a')
sidebar2


# hemisphere_link2 = []
# hemisphere_name2 = []
# 
# for hems in sidebar2:
#         name = sidebar2.find('h3').text
#         hemisphere_name2.append(name)
#         link = sidebar2.a['href']
#         hemisphere_link2.append(link)
# hemisphere_name2
# hemisphere_link2

# In[ ]:


sidebar = soup4.find('div', class_='collapsible results')
sidebar


# In[ ]:


sidebar = soup4.find('div', class_='collapsible results')
hemisphere_link = []
hemisphere_name = []

for hems in sidebar:
        name = sidebar.find('h3').text
        hemisphere_name.append(name)
        link = sidebar.a['href']
        hemisphere_link.append(link)
hemisphere_name
hemisphere_link


# #Making it a dictionary
# 
# #single entry
# 
# hem_info = {
#     'title':''
#     'img_url':''
# }
# 
# hemisphere_image_urls = [

# In[19]:


#class="itemLink product-item"
#browser.back()

links =browser.find_by_css('a.product-item img')
print (links)


# In[20]:


hemisphere_image_urls=[]
for i in range(len(links)):
        hemisphere = {}
        browser.find_by_css('a.product-item img')[i].click()
        element=browser.links.find_by_text('Sample').first
        hemisphere['img_url']=element['href']
        hemisphere['title']=browser.find_by_css('h2.title').text
        hemisphere_image_urls.append(hemisphere)
        #print(element['href'])
        browser.back()
hemisphere_image_urls


# In[ ]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]


