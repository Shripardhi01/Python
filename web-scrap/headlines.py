
# coding: utf-8

# In[12]:


def load_data1(in_url):
    data=requests.get(in_url)
    soup = BeautifulSoup(data.content, 'html.parser')
    headlines=list()
    m1=soup.select('div.news-area div.media-heading a')
    for j in m1:
        headlines.append(j.get_text(strip=True))
    make_csv1(headlines)
def make_csv1(headings):
    df = pd.DataFrame(headings, columns=None)       
    df.to_csv('Headlines.csv', index=False, header=False)

if __name__=="__main__":
    in_url="https://www.hindustantimes.com/topic/headline"  #headlines web page
    load_data1(in_url)

