import requests
from bs4 import BeautifulSoup
import lxml
import os
import openpyxl
import csv
from time import sleep

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

# req = requests.get(url=domen, headers=headers)
# src = req.text

# with open("source/chebyrashka.com.ua/chebyrashka.html", "w", encoding="UTF-8") as file:
#     file.write(src)

try:
    # with open("source/chebyrashka.com.ua/chebyrashka.html", "r", encoding="UTF-8") as file:
    #     src = file.read()
    #
    # soup = BeautifulSoup(src, "lxml")

    # products_hrefs = soup.find("div", class_="row products").find_all("div", class_="caption")
    # products_urls = []

    # for href in products_hrefs:
    #     products_url = href.find("a").get("href")
    #     products_url = href_domen + products_url
    #     products_urls.append(products_url)
    # print(products_urls)

    # n = 0
    # for i in products_urls:
    #     req = requests.get(url=i, headers=headers)
    #     src = req.text
    #
    #     b = i.split("/")
    #     with open(f"source/chebyrashka.com.ua/{n}_{b[4]}.html", "w", encoding="UTF-8") as file:
    #         file.write(src)
    #     print(f"Ссылка номер {n} сохранена!")
    #     n += 1
    #     sleep(1)

    folder_name = "source/chebyrashka.com.ua"
    nazvaniya = os.listdir(folder_name)
    nazvaniya = sorted(nazvaniya, key=sort_key_digit_getter)
    for name in nazvaniya[0:1]:
        with open(f"{folder_name}/{name}", "r", encoding="UTF-8") as file:
            src = file.read()
            soup = BeautifulSoup(src, "lxml")












except Exception as ex:
    print(ex)