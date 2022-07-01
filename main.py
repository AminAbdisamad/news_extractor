# import re
# from bs4 import BeautifulSoup as Soup
# from urllib.request import urlopen
# import requests
import json
from extractor import extract_by_class

# routers = extract(
#     url="https://www.reuters.com/business/energy/russia-decree-sakhalin-2-project-knocks-mitsui-mitsubishi-shares-2022-07-01/",
#     section="main",
#     cls_value="regular-article-layout__main__1tzD8",
# )

# print(routers)


articles = extract_by_class(
    url="https://www.economist.com/finance-and-economics/",
    section="div",
    cls_value="css-16uw8sa eprz4kh0",
)

# list = [
# {
# date:df,
# time:df,
# body : df,

# }
# ]

economist = []


for element in articles:
    t = element.find("h3", attrs={"class": "css-gvuae2 evsrcsw0"})
    title = t.a.text

    url = t.a["href"]
    main_article = extract_by_class(
        url=f"https://www.economist.com/{url}",
        section="div",
        cls_value="css-1nza9ip e89g54i0",
    )

    for article in main_article:
        date = article.find("time", attrs={"class": "css-94e3d0 e11vvcj40"})
        article_body = article.find("div", attrs={"class": "css-8oxbol e15vdjh41"})
        economist.append({"title": title, "date": date.text, "body": article_body.text})
    # body = element.find("p", attrs={"class": "css-qnkbrf ey69q3h0"})
    # date =
    # print("title ", title)
    # print("url", url)
    # print("summary", body.text)

print(json.dumps(economist, indent=4))
print()
print(economist.length)
