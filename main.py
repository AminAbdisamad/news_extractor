import json
from extract.economist import Economist

economist = Economist()
articles = economist.get_articles(
    url="https://www.economist.com/finance-and-economics",
    section="div",
    value="css-16uw8sa eprz4kh0",
)
# print(json.dumps(articles, indent=4))

# news_articles = [
#     ["url", "section", "cls"],
#     ["url", "section", "cls"],
#     ["url", "section", "cls"],
# ]

# for article in news_articles:
#     url = article[0]
#     section = article[1]
#     cls_value = article[2]
#     news = extract_by_class(url, section, cls_value)
