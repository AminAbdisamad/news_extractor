import json
from extract.economist import Economist
from extract.yenisafak import YeniSafak

economist = Economist()
ECONOMIST_PAGE_LIMIT = 272

# economist.save_csv(
#     url="https://www.economist.com/finance-and-economics",
#     section="div",
#     value="css-e6sfh4 e1mrg8dy0",
#     pages=ECONOMIST_PAGE_LIMIT,
# )


# print(json.dumps(articles, indent=4))

# number = 10
# for n in range(1, number + 1):
#     print(f"Number {n}")


# Yenisafa news
url = "https://api.piri.net/graphql/yenisafaken/"
body = """
{
feed(page:1, limit:4,filter: {contentType: null, categories: ["606cb5649e7f71a2960c11cf"] })
{
 		title
		publishDate
		url
}
}
"""

yeni = YeniSafak()
yeni.graphql(url=url, body=body)
