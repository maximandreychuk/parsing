from bs4 import BeautifulSoup
import re
with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

h1_one = soup.find('h1')
list_h1_all = soup.find_all('h1')

user_city = soup.find('div', class_ = 'user__city').find_all('span')[1].text
user_data = soup.find('div', class_ = 'user__data').find_all('span')
social_networks = soup.find('div', class_ = 'social__networks').find_all('li')

for i in social_networks:
    i = soup.find('a').get('href')
    

# .find_parent() ..find_parents()

post_div = soup.find(class_= 'post__text').find_parent('div', class_='user__post')


# .next_element .previous_element
article_name = soup.find('div', class_='post__title').next_element.next_element.text

# .find_next_sibling .find_previous_sibling 
article_txt= soup.find('div', class_='post__title').find_next_sibling()

twitter_href = soup.find(class_='social__networks').find_all('a')

find_text_maska= soup.find('a', string = re.compile('Маска')).text

find_all_text_maska = soup.find_all('a', string = re.compile('Маска'))
for i in find_all_text_maska:
    print(i.text)

print(find_all_text_maska)

