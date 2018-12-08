import requests
import time
from bs4 import BeautifulSoup
from pygame import mixer
 
url = input("Enter the url of the stock: ")
target_price = input("Enter the target price: ")
target_price = float(target_price)
mixer.init()
mixer.music.load('faith-42201.mp3')
 
while True:
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    current_price = soup.find('span', attrs={'class': 'pr'}).text
    current_price = float(current_price)
    print(current_price.text)
    if current_price > target_price:
        print("reached your target price")
        mixer.music.play()
        time.sleep(10)
        break
 
    time.sleep(10)
