import requests
import bs4
import io
import urllib
import urllib.request
import urllib.parse
import csv

with io.open('medicine.csv','a',encoding = "UTF-8") as f1:
    f1.write("med_name,med_manuf,med_gen,med_price"+ "\n")
    f1.close()
             

responce = requests.get('https://www.netmeds.com/medicine/manufacturers')
responce = responce.text
data = bs4.BeutifulSoup(responce,'lxml')
read1 = data.select(".alpha-drug-list")
print(read1)
for i in range(len(read1)):
    x = read1[i].find_all("li")
    for j in range (len(x)):
        y = x[j].find_all("a")
        for k i n range(len(y)):
            z = y[k].get("href")
            co_url.append(z)
print(z)
all_url = []
for i in range(len(co_url)):
    responce = requests.get(co_url[0])
    responce = responce.text
    data = bs4.BeautifulSoup(responce, 'lxml')
    read1 = data.select(".panel-body")
    for i in range(len(read1)):
        x = read1[i].find_all("li")
        for j in range (len(x)):
            y = x[j].find_all("a")
            for k i n range(len(y)):
                z = y[k].get("href")
                all_url.append(z)
print(len(all_url))
# print(z)
for i in range len(all_url):
    responce = requests.get(all_url[0])
    responce = responce.text
    data = bs4.BeautifulSoup(response,'lxml')
    check = data.find_all('h2',{'class' : 'title'})
    if check == []:
        med_name = data.find_all('span',{'class' : 'base'})
        med_price = data.find_all('span',{'class' : 'price'})
        med_gen = data.find_all('span',{'class' : 'gen_name'})
        med_manuf = data.find_all('a',{'class' : 'p_manuf'})
        
        with io.open('medicine.csv','a',encoding = "UTF-8") as f2:
            f2.write((med_name[0].text)+","+(med_manuf[0].text)+","+(med_gen[0].text)+","+(med_price[0].text)+"," "\n")
            f2.close()
            
    else:   
        i = i + 1
        
        
        
        
        
        
        