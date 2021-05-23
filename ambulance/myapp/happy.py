'''address=input("Enter the adress : ")
succ={}
ads=""
for a in address.split():    
    ads+=a
    ads+='+'


link="https://maps.google.com/maps?q=hospital+near"+ads+"&output=embed"
succ={"num":link}
print(succ['num'])
'''
'''
import urllib3
from bs4 import BeautifulSoup

url="https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
page=urllib3.urlopen(url)
a=BeautifulSoup(page)

print(a.find_all('a'))

'''

from bs4 import BeautifulSoup
import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
a=BeautifulSoup(r)
print(a.find_all('a'))
