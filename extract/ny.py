import requests
import os
from pprint import pprint
from dataclasses import dataclass
import json
from dotenv import load_dotenv
load_dotenv()



API_KEY = os.getenv("API_KEY")

# NY_NEWS_CATEGORIES = "Business" "Economy" "Finance" "Money"
FINANTIAL = "Financial"
BUSINESS = "Business"
MONEY = "Your Money"
NY_NEWS_CATEGORIES = (FINANTIAL, BUSINESS, MONEY)
START_DATE = "20150101"
END_DATE = "20230127"

NY_NEWS_CATEGORIES = [FINANTIAL, BUSINESS, MONEY]
r = requests.get(
    f"https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:({FINANTIAL})&api-key{API_KEY}=MyFAZqPhqGhSMqXOoxGcB4AtNbTGR3T7&page=0"
)
r.status_code
r.headers["content-type"]
data = r.json()
ny_data = []
articles = data["response"]["docs"]


# print(json.dumps(ny_data[1], indent=4))
pprint(len(articles))


# print(json.dumps(r.json(), indent=4))


# a class for ny times
# method that will gives us the data
# from categories, start date, end date, and page number
#  clean the data
# dispay data
# save csv file
# save json file


@dataclass
class NYTimes:
    def clean(self, text):
        """@description: clean the data

        @return: cleaned data
        """
        symbols = ["(", ")", ".", ",", "\u2014", "\u2019s"]
        for symbol in symbols:
            text = text.replace(symbol, "")
        return text

    def display(self):
        """@description: display the data

        @return: display the data
        """
        pass

    def main(self, categories: tuple, start_date: str, end_date: str, page: int):
        """@description: main function

        @return: main function
        """
        # data = []
        for category in categories:
            r = requests.get(
                f"https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:({category})&api-key={}&page={page}"
            )

        #     articles = r.json()["response"]["docs"]
        #     data += self.get_articles(articles)
        # return data

    def get_articles(self, articles) -> list["dict"]:
        data = []
        for article in articles:
            body = self.clean(article["abstract"])
            body += self.clean(article["lead_paragraph"])
            subject = self.clean(article["headline"]["main"])
            date = self.clean(article["pub_date"])
            keywords = " ".join(
                [self.clean(keyword["value"]) for keyword in article["keywords"]]
            )

            data.append(
                {
                    "Body": body,
                    "Subject": subject,
                    "Date": date,
                    "keywords": keywords,
                },
            )
        return data

    def save_csv(self):
        """@description: save the data as csv file

        @return: save the data as csv file
        """
        pass
