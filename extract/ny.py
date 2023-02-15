import requests
import time
import os
from datetime import date


from pprint import pprint
from dataclasses import dataclass
import json
import csv
from dotenv import load_dotenv
from . import BaseExtractor

load_dotenv()


API_KEY = os.getenv("NYT_API_KEY")

# NY_NEWS_CATEGORIES = "Business" "Economy" "Finance" "Money"

# r = requests.get(
#     f"https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:({FINANTIAL})&api-key{API_KEY}=MyFAZqPhqGhSMqXOoxGcB4AtNbTGR3T7&page=0"
# )
# r.status_code
# r.headers["content-type"]
# data = r.json()
# ny_data = []
# articles = data["response"]["docs"]


# print(json.dumps(ny_data[1], indent=4))
# pprint(len(articles))


# print(json.dumps(r.json(), indent=4))


# a class for ny times
# method that will gives us the data
# from categories, start date, end date, and page number
#  clean the data
# dispay data
# save csv file
# save json file


@dataclass
class NYTimes(BaseExtractor):
    # def clean(self, text):
    #     """@description: clean the data

    #     @return: cleaned data
    #     """
    #     symbols = ["(", ")", ".", ",", "\u2014", "\u2019s"]
    #     for symbol in symbols:
    #         text = text.replace(symbol, "")
    #     return text

    def display(self):
        """@description: display the data

        @return: display the data
        """
        pass

    def main(self, category: str, start_date: str, end_date: str, page: int):
        """@description: main function

        @return: main function
        """

        r = requests.get(
            f"https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:({category})&api-key={API_KEY}&page={page}&begin_date={start_date}&end_date={end_date}"
        )
        r.headers["content-type"]

        data = r.json()
        # print(data)

        try:
            articles = data["response"]["docs"]
        except KeyError as e:
            print(f"Error: {e}")
            print(r.status_code)
            print(r.headers)
            articles = []

        return self.get_articles(articles)

    def get_articles(self, articles) -> list["dict"]:
        data = []
        for article in articles:
            body = self.clean_text(article["abstract"])
            body += self.clean_text(article["lead_paragraph"])
            subject = self.clean_text(article["headline"]["main"])
            date = self.clean_text(article["pub_date"])
            keywords = " ".join(
                [self.clean_text(keyword["value"]) for keyword in article["keywords"]]
            )

            data.append(
                {
                    "Subject": subject,
                    "Body": body,
                    "Date": date,
                    "keywords": keywords,
                },
            )
            # Save to csv

        return data

    def save_csv(self, categories: list, start_date, end_date, page):
        with open(
            "corpus/nyt_news.csv",
            mode="a",
            encoding="utf-8",
            # append to the file,
            newline="",
        ) as nyt:
            fieldnames = ["title", "body", "date", "keywords"]
            # writer = csv.DictWriter(nyt, fieldnames=fieldnames)
            writer = csv.writer(nyt)
            writer.writerow(fieldnames)
            for category in categories:
                for page in range(120, page):
                    time.sleep(
                        5
                    )  # we want to sleep for 5 seconds before making another request to the api
                    data = self.main(category, start_date, end_date, page)
                    if not data:
                        break
                    print(f"Extracting data from page {page} of category {category}...")
                    for row in data:
                        writer.writerow(row.values())


# for category in NY_NEWS_CATEGORIES:
#     for page in range(PAGE_NUMBER):
#         # sleep for 2 second before making another request
#         time.sleep(5)
#         data = ny.main(
#             category=category, start_date=START_DATE, end_date=END_DATE, page=page
#         )

#         if not data:
#             break
#         print(f"Extracting data from page {page} of category {category}...")
#         ny.save_csv(data)
# for page in range(PAGE_NUMBER):
# data = ny.main(
#     category=NY_NEWS_CATEGORIES, start_date=START_DATE, end_date=END_DATE, page=1
# )
# ny.save_csv(data)
# print(json.dumps(data, indent=4))


# data = ny.main(category=MONEY, start_date=START_DATE, end_date=END_DATE, page=0)
# print(json.dumps(data, indent=4))

# pprint(t)


# !@description: Please start at 120 for business category next ime
# ! and 0 from the other categories
