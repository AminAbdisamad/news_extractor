import requests
import json

# NY_NEWS_CATEGORIES = "Business" "Economy" "Finance" "Money"
FINANTIAL = "Financial"
BUSINESS = "Business"
MONEY = "Your Money"

NY_NEWS_CATEGORIES = [FINANTIAL, BUSINESS, MONEY]
r = requests.get(
    f"https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:({MONEY})&begin_date=20150101&end_date=20521029&api-key=MyFAZqPhqGhSMqXOoxGcB4AtNbTGR3T7"
)
r.status_code
r.headers["content-type"]
r.encoding
# print(r.content)
r.text
data = r.json()
ny_data = []
articles = data["response"]["docs"]

for article in articles:
    ny_data.append(
        {
            "Abstract": article["abstract"],
            "Lead Pragraph": article["lead_paragraph"],
            "Subject": article["headline"]["main"],
        },
    )

print(json.dumps(ny_data, indent=4))


# print(json.dumps(r.json(), indent=4))
