import csv

# read from csv file with [date, title, url]
# using the url get the full article
# save the full article to csv file with [date, title, body]


# Path: selenium/daily_sabah.py


def read_csv():
    urls = []
    with open(
        "corpus/daily_sabah_summary.csv", mode="r", encoding="utf-8", newline=""
    ) as f:
        reader = csv.DictReader(f)
        for row in reader:
            urls.append(row.get("url"))
        return urls


# Scraping the full article
# def get_full_articles(urls):
#     data = []
#     for url in urls:
#         article_info = find(
#             url=url,
#             section="div",
#             value="css-1f1k1f8 e1prll3w0",
#         )
#         data.append(article_info)
#     return data
