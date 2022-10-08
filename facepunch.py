## Importing packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

## Pulling website
# I chose this site as it has a lot of data and is easy to scrape
# This site provides commits from a game studio called "Facepunch"
page = requests.get('https://commits.facepunch.com/') 

## Creating a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

## Print Pretty
print(soup.prettify())

## Getting the title for the commits
fp_repo = soup.find_all('span' ,class_='repo')
fp_branch = soup.find_all('span' ,class_='branch')
fp_id = soup.find_all('span' ,class_='changeset')

## Creating title
# Title Repo
fp_output_repo = []
for i in fp_repo:
    print(i.text)
    data = i.text
    fp_output_repo.append(data)

len(fp_output_repo)
fp_output_repo[1]
fp_output_repo[2]

# Title Branch
fp_output_branch = []
for i in fp_branch:
    print(i.text)
    data = i.text
    fp_output_branch.append(data)

len(fp_output_branch)
fp_output_branch[1]
fp_output_branch[2]

# Title ID
fp_output_id = []
for i in fp_id:
    print(i.text)
    data = i.text
    fp_output_id.append(data)

len(fp_output_id)
fp_output_id[1]
fp_output_id[2]

## Creating combined title
fp_combined_title = []
length = len(fp_output_repo)
count = 0
if count != length:
    for i in fp_output_repo:
        title = fp_output_repo[count] + fp_output_branch[count] + fp_output_id[count]
        fp_combined_title.append(title)
        count = count + 1
fp_combined_title[1]
fp_combined_title[2]

## Getting the descriptions for the commits
fp_descriptions = soup.find_all('div' ,class_='commits-message')

fp_output_description = []
for i in fp_descriptions:
    print(i.text)
    data = i.text
    fp_output_description.append(data)

len(fp_output_description)
fp_output_description[1]
fp_output_description[10]

## Getting the time for the commits
fp_time = soup.find_all('div' ,class_='time')

fp_output_time = []
for i in fp_time:
    print(i.text)
    data = i.text
    fp_output_time.append(data)

len(fp_output_time)
fp_output_time[1]
fp_output_time[10]

## Creating a dataframe with all the information
df = pd.DataFrame({'commit_title': fp_combined_title, 'commit_description': fp_output_description, 'commit_time': fp_output_time})

## Saving dataframe to csv
df.to_csv('data/facepunch_commmits.csv')