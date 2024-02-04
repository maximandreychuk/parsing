import requests
from bs4 import BeautifulSoup
import json
import csv

headers ={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15"
}
# url_base = "https://health-diet.ru"
# url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
# req = requests.get(url, headers=headers)
# src = req.text
# with open("index.html") as file:
#     src = file.read()
# soup = BeautifulSoup(src, "lxml")


# all_categories_dict = {}
# href_products = soup.find_all(class_="mzr-left-menu-item uk-link-reset")
# for i in href_products:
#     all_categories_dict[i.text] = url_base + i.get("href")


# with open('all_categories_dict.json', 'w') as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
with open('all_categories_dict.json') as file:
    all_categories_dict = json.load(file)


count = 0

for category_name, category_href in all_categories_dict.items():


    rep = [",", "-", " ", "\n"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")

    req = requests.get(url=category_href, headers=headers)
    src = req.text
    
    with open(f"data/{count}{category_name}.html", 'w') as file:
        file.write(src)
    
    with open(f"data/{count}{category_name}.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    alert_block = soup.find(class_="uk-alert-danger")
    if alert_block is not None:
        continue

    headers_of_products = f'headers_of_{category_name}'
    headers_of_products = soup.find("thead").find_all("th")
    product = headers_of_products[0].text
    calories = headers_of_products[1].text
    proteins = headers_of_products[2].text
    fats = headers_of_products[3].text
    carbohydrates = headers_of_products[4].text
    with open(f"data/{count}_{category_name}.csv", "w", encoding = "utf-8") as file:
        writer = csv.writer(file)
        writer.writerow((
            product,
            calories,
            proteins,
            fats,
            carbohydrates
        )
        )

    products_data = soup.find("tbody").find_all("tr")
    for i in products_data:
        products_tds = i.find_all("td")
        title = products_tds[0].find("a").text
        calories = products_tds[1].text
        proteins = products_tds[2].text
        fats = products_tds[3].text
        carbohydrates = products_tds[4].text

        with open(f"data/{count}_{category_name}.csv", "a", encoding = "utf-8") as file:
            writer = csv.writer(file)
            writer.writerow((
                title,
                calories,
                proteins,
                fats,
                carbohydrates
            )
            )

    count += 1

