## Importing packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

## Pulling website
# I chose this site because it seemed like something different to scrape
# I originally wanted to pull information from USAJOBS, but I ran into so many errors
page = requests.get('https://www.cyberpowerpc.com/category/esports-gaming-pcs/') 

## Creating a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

## Getting the Name for the PC
pc_title = soup.find_all('h2' ,class_='g-sys-name')

pc_opt_titles = []
for i in pc_title:
    print(i.text)
    data = i.text
    pc_opt_titles.append(data)

len(pc_opt_titles)
pc_opt_titles[0]
pc_opt_titles[5]

## Getting the GPU for the PC
pc_gpu = soup.find_all('ul' ,class_='g-sys-spec')

pc_opt_spec = []
for i in pc_gpu:
    print(i.text)
    data = i.text
    pc_opt_spec.append(data)

len(pc_opt_spec)
pc_opt_spec[0]
pc_opt_spec[5]

## Getting the Price for the PC
pc_price = soup.find_all('p' ,class_='g-sys-price')

pc_opt_price = []
for i in pc_price:
    print(i.text)
    data = i.text
    pc_opt_price.append(data)

len(pc_opt_price)
pc_opt_price[0]
pc_opt_price[5]

## Getting Shipping Price for the PC
pc_ship = soup.find_all('span' ,class_='g-sys-fs')

pc_opt_ship = []
for i in pc_ship:
    print(i.text)
    data = i.text
    pc_opt_ship.append(data)

len(pc_opt_ship)
pc_opt_ship[0]

## Creating a dataframe with all the information
df = pd.DataFrame({'pc_name': pc_opt_titles, 'specs': pc_opt_spec, 'price': pc_opt_price, 'shipping status': pc_opt_ship})

## Saving dataframe to csv
df.to_csv('data/cyberpower_pcs.csv')