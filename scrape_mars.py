#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:

def scrape_info():
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)


        # In[3]:


        url = 'https://redplanetscience.com/'
        browser.visit(url)


        # In[4]:


        # for none DYNAMIC CONTENT
        # response = requests.get(url)
        # soup = bs(response.text, 'lxml') #html.parser
        # print(soup.prettify())


        # In[5]:


        html = browser.html
        soup = bs(html, 'lxml')


        # In[6]:


        #print(soup.prettify())


        # In[7]:


        results = soup.find_all('div', class_='list_text')


        # In[8]:


        news_names = []
        for result in results:
                news = {}
                # Identify and return title of listing
                title = result.find(class_='content_title').text
                news['title'] = title
                # Identify and return teaser of listing
                teaser = result.find(class_='article_teaser_body').text
                news['teaser'] = teaser
                news_names.append(news)

        #         # Print results only if title, price, and link are available
        #         print('-------------')
        #         print(title)
        #         print(teaser)
        print (news_names)


        # In[9]:


        url2 = 'https://spaceimages-mars.com/'
        browser.visit(url2)
        html = browser.html
        soup2 = bs(html, 'lxml')


        # In[10]:


        #print(soup2.prettify())


        # In[11]:


        featured_image = soup2.find(class_='showimg fancybox-thumbs')
        featured_image


        # In[12]:


        featured_image_url = format(featured_image.get('href'))
        featured_image_url_final = url2 + featured_image_url
        featured_image_url_final


        # In[13]:


        url3 = 'https://galaxyfacts-mars.com/'
        tables = pd.read_html(url3)
        #tables


        # In[14]:


        planet_facts_df = tables[0]
        planet_facts_df.set_index(0,inplace= True)
        planet_facts_df


        # In[15]:

        # list_factors = planet_facts_df[0].to_list()
        # list_factors

        # list_mars = planet_facts_df[1].to_list()
        # list_mars

        # list_earth = planet_facts_df[2].to_list()
        # list_earth

        #mars_facts_table = planet_facts_df.to_html()


        # In[16]:


        url4 = 'https://marshemispheres.com/'
        browser.visit(url4)
        html = browser.html
        soup4 = bs(html, 'lxml')


        # In[17]:


        #print(soup4.prettify())


        # In[18]:


        links =browser.find_by_css('a.product-item img')
        #print (links)


        # In[19]:

        #count = 0
        hemisphere_image_urls=[]
        for i in range(len(links)):
                hemisphere = {}
                browser.find_by_css('a.product-item img')[i].click()
                element=browser.links.find_by_text('Sample').first
                hemisphere['title']=browser.find_by_css('h2.title').text
                hemisphere['img_url']=element['href']
                hemisphere_image_urls.append(hemisphere)
                browser.back()
        hemisphere_image_urls


        # In[20]:

        mars_data = {
                "news_names1" : news_names[0],
                "mars_image" : featured_image_url_final,
                #"mars_table" : mars_facts_table,
                # "mars_factors" : list_factors,
                # "mars_mars" : list_mars,
                # "mars_earth" : list_earth,
                "hemisphere_info": hemisphere_image_urls
        }

        browser.quit()

        return mars_data

