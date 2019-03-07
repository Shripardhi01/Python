
# coding: utf-8

# In[283]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

def load_data(in_url):
    data=requests.get(in_url)
    soup = BeautifulSoup(data.content, 'html.parser')
    tags=['h1 a','h2 a','h3 a','div.news-area div.media-heading a',
          'div.news-area div.random-content.clearfix div.random-tx.clearfix div.para-txt a']
    headlines=list()
    for i in tags:
        m1=soup.select(i)
        for j in m1:
            headlines.append(j.get_text(strip=True))
    make_csv(headlines)
def make_csv(headings):
    df = pd.DataFrame(headings, columns=None)       
    df.to_csv('Headlines_from_homepage.csv', index=False, header=False)

if __name__=="__main__":
    in_url="https://www.hindustantimes.com/"             #Homepage url
    load_data(in_url)

