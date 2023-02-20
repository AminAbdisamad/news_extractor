import requests
import csv
import time
from pprint import pprint
from datetime import datetime
from time import sleep
from . import BaseExtractor


# ys-detail-content

date_format = "%d/%m/%y"


class YeniSafak(BaseExtractor):
    BASE_URL = "https://www.yenisafak.com/en"
    # "https://www.yenisafak.com/en/economy/turkiye-to-receive-14b-cubic-meters-of-gas-from-oman-per-year-3659808"
    def get_article_meta(self, *, url: str, body: str):
        yenisafak = []
        # change to Turkiye everwhere theres  T\u00fcrkiye
        word = "Turkiye"
        comma = "'"

        status_code, content = self.graphql(url=url, body=body)
        if status_code == 200:

            data = content["data"]["feed"]
            for article in data:

                yenisafak.append(
                    {
                        "date": datetime.fromisoformat(
                            article.get("publishDate").replace("Z", "+00:00")
                        ).strftime("%B %d %Y"),
                        "title": article.get("title")
                        .replace("T\u00fcrkiye", word)
                        .replace("\u2019", comma),
                        "summary": article.get("spot"),
                        # "url": self.BASE_URL + article.get("url"),
                    }
                )

        self.save_csv(data=yenisafak)

    def save_csv(self, *, data: list):

        with open(
            "corpus/yenisafak.csv",
            mode="a",
            encoding="utf-8",
            # append to the file,
            newline="",
        ) as nyt:
            fieldnames = ["date", "title", "summary"]
            # writer = csv.DictWriter(nyt, fieldnames=fieldnames)
            writer = csv.writer(nyt)
            writer.writerow(fieldnames)
            for row in data:
                print("Extracting data from Yeni Safak")
                writer.writerow(row.values())


YENI_SAFAK_QUERY = """
    {
    feed(page:1, limit:5050,filter: {contentType: null, categories: ["606cb5649e7f71a2960c11cf"] })
    {
            title
            publishDate
            url
            spot
    }
    }
    """
