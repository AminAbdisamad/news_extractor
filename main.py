import json
from extract.economist import Economist
from extract.ny import NYTimes
from extract.yenisafak import YeniSafak, YENI_SAFAK_QUERY

# Economist
def extract_from_economist():
    economist = Economist()
    ECONOMIST_PAGE_LIMIT = 273

    economist.save_csv(
        url="https://www.economist.com/finance-and-economics",
        section="div",
        value="css-e6sfh4 e1mrg8dy0",
        pages=ECONOMIST_PAGE_LIMIT,
    )


# nytimes
def extract_from_nytimes():
    ny = NYTimes()
    NY_NEWS_CATEGORIES = ["Business", "Your Money", "Financial", "Economic Analysis"]
    START_DATE = "20150101"
    END_DATE = "20230127"
    PAGE_NUMBER = 201
    ny.save_csv(NY_NEWS_CATEGORIES, START_DATE, END_DATE, PAGE_NUMBER)


def extract_from_yenisafak():
    # Yenisafa news
    url = "https://api.piri.net/graphql/yenisafaken/"
    yeni = YeniSafak()
    articles = yeni.get_article_meta(url=url, body=YENI_SAFAK_QUERY)
    print(json.dumps(articles, indent=4))
    # limit 5050


if __name__ == "__main__":
    # extract_from_nytimes()
    extract_from_yenisafak()
