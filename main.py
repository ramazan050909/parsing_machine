import csv
import requests
from bs4 import BeautifulSoup as BS


data = []
for i in range(1,11):
    URL = f'https://www.mashina.kg/motosearch/all/?page={i}'

    response = requests.get(URL)
    soup = BS(response.text, 'html.parser')
    products = soup.find_all('div', class_='list-item')

    for product in products:
        title = product.find('h2', class_='name').text
        price = product.find('p', class_='price').text
        image = product.find('img').get('data-src')
        description = product.find('p', class_='body-type').text
        product_info = [title, price, image, description]
        data.append(product_info)
    
def write_csv(ms):
    with open('mashina_kg.csv','w') as file:
        writer = csv.writer(file)
        writer.writerow(['Наименование', 'Цена', 'Ссылка на изображение', 'Краткое описание'])
        for row in ms:
            writer.writerow(row)

print(len(data))
write_csv(data)
