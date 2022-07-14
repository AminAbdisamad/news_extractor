from extract import Extractor


class Economist(Extractor):
    def get_articles(self, *, url, section, value):
        articles = self.find(url=url, section=section, value=value)
        links = self.get_single_article_url(articles)
        data = self.get_body(links)
        return data

    def get_single_article_url(self, articles):
        article_url = []
        for link in articles:
            t = link.find("h3", attrs={"class": "css-1e1hbwe evsrcsw0"})
            url = t.a["href"]
            article_url.append(url)
        return article_url

    def get_body(self, links):
        data = []
        articles = []
        for link in links:
            body = self.find(
                url=f"https://www.economist.com/{link}",
                section="div",
                value="css-1nza9ip e89g54i0",
            )
            articles.append(body)
        for article in articles[0]:
            date = article.find("time", attrs={"class": "css-94e3d0 e11vvcj40"})
            body = article.find("div", attrs={"class": "css-1jx1v8p e15vdjh41"})
            subject = article.find("h1", attrs={"class": "css-1bo5zl0 eoacr0f0"})
            print({"date": date.text, "body": body.text, "title": subject.text})
            # data.append({"title": subject.text, "date": date.text, "body": body.text})
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
