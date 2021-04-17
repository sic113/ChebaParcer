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


domen = "https://chebyrashka.com.ua/ru/detskaya-obuv?limit=300"
href_domen = "https://chebyrashka.com.ua/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.344",
    "accept":"application/signed-exchange;v=b3;q=0.9,*/*;q=0.8"
}



req = requests.get(url=domen, headers=headers)
src = req.text

# Получаем главный html
with open("data/obuv.html", "w", encoding="UTF-8") as file:
    file.write(src)



try:
    # Открываем главный html
    with open("data/obuv.html", "r", encoding="UTF-8") as file:
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
    n = 0
    for i in products_urls:
        req = requests.get(url=i, headers=headers)
        src = req.text

        b = i.split("/")
        with open(f"data/obuv/{n}_{b[4]}.html", "w", encoding="UTF-8") as file:
            file.write(src)
        print(f"Ссылка номер {n} сохранена!, осталось {len(products_urls) - n}")
        n += 1

except Exception as ex:
    print(ex)



try:
    folder_name = "data/obuv"
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
                razm = soup.find("div", class_="radio").text
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
                other_hrefs = soup.find("div",class_="thumbnails image-additional").findAll("a")
                other_hrefs_str = ""
                # print(other_hrefs)
                for i in other_hrefs:
                    href = i.get("href")
                    other_hrefs_str = other_hrefs_str+href_domen+href+"\n"
                    # print(href)
                other_hrefs_str = other_hrefs_str+href_main
            except:
                other_hrefs = "-"
            # print(other_hrefs_str)

            with open("data/obuv.csv", "a", newline='', encoding="UTF-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        art,
                        opis,
                        nazv,
                        razm,
                        other_hrefs_str,
                        price
                    )
                )


            print(f"Товар номер {n} с артикулом {art} успешно добавлен в csv таблицу, осталось {len(nazvaniya) - n}")
            n += 1


except Exception as ex:
    print(ex)

