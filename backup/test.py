i = "https://chebyrashka.com.ua/ru/krossovki-detskie-m-boan-chernye-s-belym?limit=300"
i = i.split("/")
print(i[4])

try:
    opis = soup.find("div", id="tab-description").text
    opis = opis.strip()
    video_link = soup.find("div", id="tab-description").find("a").get("href")
    # print(video_link)
    opis = opis + "\n" + video_link
    opis = opis.strip()
except:
    opis = "-"



video_link = soup.find("div", id="tab-description").find("a").get("href")
# print(video_link)
opis = opis + "\n" + video_link
opis = opis.strip()