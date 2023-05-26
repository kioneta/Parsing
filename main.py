import requests
from bs4 import BeautifulSoup
from time import sleep

headers =  { 
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}


def array ():
    N = 0
    for count in range (1, 7):
        sleep(3) #перерыв на 3 сек
        url = f"https://www.bambytoys.ru/catalog/65_8_gaga_nast_igry_iz_vo_protiv_zavedeniya_klientami_ikh_produktsii_na_markerpleysy_/?PAGEN_1={count}" #проходим по страницам+
        response = requests.get(url, headers=headers)  # получение ответа от сайта
        soup = BeautifulSoup(response.text, "lxml")  # html.parser - доп вариант помощи bs4
        data = soup.find_all("div", class_="bx_catalog_item double")  # находим как оформлены нужные контейнеры

        for i in data:
            N += 1
            name = i.find("div", class_="bx_catalog_item_title").text.split('"')[1] #выводим только название в ковычках
            price = float(i.find("div", class_ = "bx_catalog_item_price").text.replace(" ", "")[:-5]) #убираем лишний текст и пробелы
            volume = i.find("div", class_ = "bx_catalog_item_count").text.strip()
            picture = i.find ("a", class_ ="bx_catalog_item_images").get("href")
            yield N, name, price, volume, picture

