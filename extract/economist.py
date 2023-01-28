from extract import BaseExtractor


class Economist(BaseExtractor):
    def get_articles(self, *, url, section, value):
        articles = self.find(url=url, section=section, value=value)
        links = self.get_single_article_url(articles)
        data = self.get_full_articles(links)
        return data

    def get_single_article_url(self, articles):
        article_url = []
        for link in articles:
            t = link.find("h3", attrs={"class": "css-juaghv eifj80y0"})
            url = t.a["href"]
            article_url.append(url)
        return article_url

    def get_full_articles(self, links):
        data = []
        full_articles = []
        for link in links:

            article_info = self.find(
                url=f"https://www.economist.com/{link}",
                section="div",
                value="css-ocg69 emzywpa0",
            )
            full_articles.append(article_info)
        for articles in full_articles:
            for article in articles:
                date = article.find("time", attrs={"class": "css-j5ehde e1fl1tsy0"})
                body = article.find(
                    "div",
                    attrs={"class": "css-13gy2f5 e1prll3w0"},
                )
                subject = article.find("h1", attrs={"class": "css-1bo5zl0 e164j1a30"})

                # print({"date": date.text, "body": body.text, "title": subject.text})
                data.append(
                    {
                        "title": self.clean_text(subject.text),
                        "date": self.clean_text(date.text),
                        "body": self.clean_text(body.text),
                    }
                )
        return data


#     for article in main_article:
#         date = article.find("time", attrs={"class": "css-94e3d0 e11vvcj40"})
#         article_body = article.find("div", attrs={"class": "css-8oxbol e15vdjh41"})
#         economist.append({"title": title, "date": date.text, "body": article_body.text})
#     # body = element.find("p", attrs={"class": "css-qnkbrf ey69q3h0"})
#     # date =
#     # print("title ", title)
#     # print("url", url)
#     # print("summary", body.text)


# print()
# print(economist.length)
