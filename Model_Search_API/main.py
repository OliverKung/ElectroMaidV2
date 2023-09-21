## author:Olvk 
## input:model you wanna search,download PDF or not
## output:the description of search model from semiee,and download PDF from semiee.
## date:230921

from selenium import webdriver
from bs4 import BeautifulSoup
import os
option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_experimental_option('excludeSwitches',['enable-logging'])
url = "https://www.semiee.com/search?searchModel="
url_download="https://www.semiee.com/"
model = input()
driver = webdriver.Chrome(options=option)
res = driver.get(url+model)
html = driver.page_source
print("get HTML success!")
driver.quit()
soup = BeautifulSoup(html,'html.parser')
search_result = soup.find_all('div', class_="result-one")[0]
model_id = search_result.get('data-modelid')
# print(search_result)
print(str(search_result.find_all("p")[1]).replace("<p>","").replace("</p>",""))
print("----------------------------------------------------------------------------------------------")

driver = webdriver.Chrome(options=option)
res = driver.get(url_download+model_id+".html")
html = driver.page_source
driver.quit()
soup = BeautifulSoup(html,'html.parser')
link = soup.find_all('li',class_="openFile")[0].get("data-href")
os.system("wget.exe -P ./Download_PDF/ "+link)
