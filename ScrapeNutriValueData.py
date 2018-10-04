import pandas as pd
import requests
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def level_one(main_page_url):
    response = requests.get(main_page_url)
    soup = BeautifulSoup(response.content,'html.parser')
    s1 = soup.find_all("a",{'class':'l'})
    topic_lists=[]
    for i in s1:
        topic = i.text
        link = i['href']
        if str(link).startswith('foods_start_with'):
            continue
        if str(link).startswith('/foods_by_'):
            link = "https://www.nutritionvalue.org" + link
        if str(link).endswith('.html'):
            link = link[:-5]+'_page_'
        else:
            link = link+"&page="
        topic_dict={}
        topic_dict['link']=link
        topic_dict['topic']=topic
        topic_lists.append(topic_dict)
    return topic_lists
# testing
# level_one('https://www.nutritionvalue.org/')

def get_number_page(topic_url, number):
    if str(topic_url).endswith("_"):
        page = topic_url+str(number)+".html"
    else:
        page = topic_url+str(number)
    return page
# testing
# get_number_page('https://www.nutritionvalue.org/search.php?category=Cereal+Grains+and+Pasta&page=',5)

def parseTitleLinks(topic_dict, limit=50):
    topic = topic_dict['topic']
    topic_url = topic_dict['link']
    print("----------------Parsing "+ str(topic) +"----------------")
    print("Parsing Page 1")
    # initialize browser
    browser = webdriver.Chrome() 
    wait = WebDriverWait(browser,2)
    # read the main website
    browser.get(get_number_page(topic_url,1))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > table > tbody > tr:nth-child(3) > td > table')))
    html = browser.page_source
    soup = BeautifulSoup(html,'html.parser')
    # scrape all url links and add them to the list
    title_links = []
    for i in soup.select('td.results.left'):
        dic = {}
        link = i.find('a')['href']
        title = i.find('a')['title']
        dic['link']='https://www.nutritionvalue.org'+link
        dic['title']=title
        dic['topic']=topic
        title_links.append(dic)
    # the total number of pages
    total_page_number = int(soup.select('th.left.results')[0].find_all('a')[-1].text)
    # quit the browser
    browser.quit()

    if total_page_number > limit:
        total_page_number = limit
        
    for m in range(2,total_page_number+1):
        print("Parsing page " + str(m))
        browser = webdriver.Chrome()
        wait = WebDriverWait(browser,2)
        # read the main page
        browser.get(get_number_page(topic_url,m))
        topic_url
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > table > tbody > tr:nth-child(3) > td > table')))
        html = browser.page_source
        soup = BeautifulSoup(html,'html.parser')
        for i in soup.select('td.results.left'):
            dic = {}
            link = i.find('a')['href']
            title = i.find('a')['title']
            dic['link']='https://www.nutritionvalue.org'+link
            dic['title']=title
            dic['topic']=topic
            title_links.append(dic)
        browser.quit()
    print("----------------Parsed "+str(topic) +"----------------")
    return title_links
# testing
# parseTitleLinks('hello world','https://www.nutritionvalue.org/search.php?category=Soups%2C+Sauces%2C+and+Gravies&page=')

def get_downlad_url():
    main_url = 'https://www.nutritionvalue.org/'
    topics_list = level_one(main_url)
    title_list = []
    topics_list = topics_list[0:1]
    for i in topics_list:
        start = time.time()
        new_list = parseTitleLinks(i,limit=208)
        end = time.time()
        duration = end - start
        print("  -------Topic Parsing Time: %6.2f s-------" % (end-start) )
        title_list.extend(new_list)
    return title_list

links = get_downlad_url()
l = []
count = 0

for htmlLink in links[count:]:
    topic = htmlLink['topic']
    title = htmlLink['title']
    response = requests.get(htmlLink['link'])
    soup = BeautifulSoup(response.content,'html.parser')
    for i in soup.select('a[target="_blank"]'):
        if len(i.text)==10:
            link = 'https://www.nutritionvalue.org' + i['href']
    l.append(link)
    print("link " + str(count) + " downloaded")
    count = count + 1

pds = pd.DataFrame(links)
del pds['link']
pds['link'] = l
pds.to_csv('newLinks.csv')

