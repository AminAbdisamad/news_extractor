import requests
from pprint import pprint
from time import sleep
from . import BaseExtractor

# ys-detail-content


class YeniSafak(BaseExtractor):
    BASE_URL = "https://www.yenisafak.com/en"
    # "https://www.yenisafak.com/en/economy/turkiye-to-receive-14b-cubic-meters-of-gas-from-oman-per-year-3659808"
    def get_article_meta(self, *, url: str, body: str):
        yenisafak = []

        status_code, content = self.graphql(url=url, body=body)
        if status_code == 200:

            data = content["data"]["feed"]
            for article in data:
                yenisafak.append(
                    {
                        "title": article.get("title"),
                        "summary": article.get("spot"),
                        "date": article.get("publishDate"),
                        # "url": self.BASE_URL + article.get("url"),
                    }
                )

        return yenisafak

    # def get_full_article(self, *, urls: str):
    #     data = []
    #     for url in urls:

    #         title = self.find_with_urlopen(
    #             url=url, section="p", value="ys-paragraph-node"
    #         )
    #         date = self.find_with_urlopen(
    #             url=url, section="p", value="ys-paragraph-node"
    #         )
    #         body = self.find_with_urlopen(
    #             url=url, section="p", value="ys-paragraph-node"
    #         )

    #         formatted_body = " ".join([self.clean_text(p.text) for p in r])

    # yenisafak.append({"body": article.get("body")})


# 5050


YENI_SAFAK_QUERY = """
    {
    feed(page:1, limit:14,filter: {contentType: null, categories: ["606cb5649e7f71a2960c11cf"] })
    {
            title
            publishDate
            url
            spot
    }
    }
    """
