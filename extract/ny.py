import requests
from pprint import pprint
import json

# NY_NEWS_CATEGORIES = "Business" "Economy" "Finance" "Money"
FINANTIAL = "Financial"
BUSINESS = "Business"
MONEY = "Your Money"
NY_NEWS_CATEGORIES = (FINANTIAL, BUSINESS, MONEY)

NY_NEWS_CATEGORIES = [FINANTIAL, BUSINESS, MONEY]
r = requests.get(
    f"https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:({MONEY})&begin_date=20150101&end_date=20230127&api-key=MyFAZqPhqGhSMqXOoxGcB4AtNbTGR3T7"
)
r.status_code
r.headers["content-type"]
data = r.json()
ny_data = []
articles = data["response"]["docs"]


def clean(text):
    symbols = ["(", ")", ".", ",", "\u2014", "\u2019s"]
    for symbol in symbols:
        text = text.replace(symbol, "")
    return text


for article in articles:
    # strip spaces trailing and leading \u
    body = clean(article["abstract"])
    body += clean(article["lead_paragraph"])
    subject = clean(article["headline"]["main"])
    date = clean(article["pub_date"])
    keywords = " ".join([clean(keyword["value"]) for keyword in article["keywords"]])

    ny_data.append(
        {
            "Body": body,
            "Subject": subject,
            "Date": date,
            "keywords": keywords,
        },
    )

print(json.dumps(ny_data[1], indent=4))
# pprint(data)


# print(json.dumps(r.json(), indent=4))
