import requests
from time import sleep
from . import BaseExtractor

# ys-detail-content


class YeniSafak(BaseExtractor):
    BASE_URL = "https://www.yenisafak.com/en"
    # "https://www.yenisafak.com/en/economy/turkiye-to-receive-14b-cubic-meters-of-gas-from-oman-per-year-3659808"
    def get_articles(self, *, url: str, body: str):
        yenisafak = []
        status_code, content = self.graphql(url=url, body=body)
        if status_code == 200:

            data = content["data"]["feed"]
            for article in data:
                yenisafak.append(
                    {
                        "title": article["title"],
                        "date": article["publishDate"],
                        "url": self.BASE_URL + article["url"],
                    }
                )
        sleep(5)
        print(yenisafak)
        for article in yenisafak:

            r = self.find_with_urlopen(
                url=article["url"], section="p", value="ys-paragraph-node"
            )

            article["body"] = " ".join([self.clean_text(p.text) for p in r])

            yenisafak.append({"body": article["body"]})
        # print(yenisafak)
        return yenisafak
        # print(yenisafak)


# 5050
