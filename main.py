import json
from extract.economist import Economist


economist = Economist()
ECONOMIST_PAGE_LIMIT = 272

economist.save_csv(
    url="https://www.economist.com/finance-and-economics",
    section="div",
    value="css-e6sfh4 e1mrg8dy0",
    pages=ECONOMIST_PAGE_LIMIT,
)


# print(json.dumps(articles, indent=4))

# number = 10
# for n in range(1, number + 1):
#     print(f"Number {n}")
