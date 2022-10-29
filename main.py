import json
from extract.economist import Economist


economist = Economist()
ECONOMIST_PAGE_LIMIT = 266

articles = economist.get_articles(
    url="https://www.economist.com/finance-and-economics?page=1",
    section="div",
    value="css-mi70rv e16rqvvr0",
)


print(json.dumps(articles, indent=4))

# number = 10
# for n in range(1, number + 1):
#     print(f"Number {n}")
