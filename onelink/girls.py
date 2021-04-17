import requests
from bs4 import BeautifulSoup
import lxml
import os
import openpyxl
import csv
from time import sleep

# Сортировка списка
def sort_key_digit_getter(row):
    raw_digit, *_ = row.split("_")
    return int(raw_digit)
# sorted(list_, key=sort_key_digit_getter)


domen = "https://chebyrashka.com.ua/ru/detskaya-odezhda-dlya-devochek?limit=400"
href_domen = "https://chebyrashka.com.ua/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

req = requests.get(url=domen, headers=headers)
src = req.text

# Получаем главный html
# with open("data/girls.html", "w", encoding="UTF-8") as file:
#     file.write(src)

"""

try:
    # Открываем главный html
    with open("data/girls.html", "r", encoding="UTF-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    # находим ссылки на каждый товар
    products_hrefs = soup.find("div", class_="row products").find_all("div", class_="caption")
    products_urls = []


    # модифицируем ссылку
    for href in products_hrefs:
        products_url = href.find("a").get("href")
        products_url = href_domen + products_url
        products_urls.append(products_url)
    print(products_urls)


    # записываем html каждого товара
    n = 218
    for i in products_urls[218:]:
        req = requests.get(url=i, headers=headers)
        src = req.text

        b = i.split("/")
        with open(f"data/girls/{n}_{b[4]}.html", "w", encoding="UTF-8") as file:
            file.write(src)
        print(f"Ссылка номер {n} сохранена!, осталось {len(products_urls) - n}")
        n += 1

except Exception as ex:
    print(ex)

"""

try:
    folder_name = "data/girls"
    nazvaniya = os.listdir(folder_name)
    nazvaniya = sorted(nazvaniya, key=sort_key_digit_getter)

    n = 0

    # открываем каждый товар
    for name in nazvaniya:
        with open(f"{folder_name}/{name}", "r", encoding="UTF-8") as file:
            src = file.read()
            soup = BeautifulSoup(src, "lxml")

            try:
                nazv = soup.find("h1", class_="h2").text
            except:
                nazv = "-"

            try:
                art = soup.find("div", class_="h2").find("small").text
                art = art.split(" ")
                art = art[2]
                art = art.replace(")","")
            except:
                art = "-"

            try:
                opis = ""
                opis_list = soup.find("div", id="tab-description").findAll("p")
                for i in opis_list:
                    opis = opis + i.text + "\n"
                opis = opis.replace(" ","")
            except:
                opis = "-"

            try:
                razm = soup.find("div", class_="form-group required").text
                razm = razm.replace("Размер","")
                razm = razm.strip()
            except:
                razm = "-"

            try:
                video_link = soup.find("div", id="tab-description").find("a").get("href")
            except:
                video_link = ""

            opis = opis + video_link


            try:
                price = soup.find("span", class_="price").text
            except:
                price = "-"

            try:
                href_main = soup.find("div",class_="thumbnails image-thumb").find("a",class_="thumbnail").get("href")
                href_main = href_domen+href_main
            except:
                href_main = "-"


            try:
                dosup = soup.find("div",class_="stock-5").text
                dostup = dosup.split(":")
                dostup = dostup[1]
                dostup = dostup.strip()
            except:
                dostup = "-"

            if dostup == "Нет в наличии":
                otobraj = "Нет"
            elif dostup == "На складе":
                otobraj = "Да"
            elif dostup == "-":
                otobraj = "Нет"

            with open("girls.csv", "a", newline='', encoding="UTF-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        art,
                        opis,
                        nazv,
                        razm,
                        href_main,
                        price,
                        dostup,
                        otobraj
                    )
                )


            print(f"Товар номер {n} с артикулом {art} успешно добавлен в csv таблицу, осталось {len(nazvaniya) - n}")
            n += 1


except Exception as ex:
    print(ex)

