import requests
from bs4 import BeautifulSoup

# define the URLs of the news websites
nyt_url = "https://www.nytimes.com/section/business"
economist_url = "https://www.economist.com/business-finance"
wsj_url = "https://www.wsj.com/news/business"
ft_url = "https://www.ft.com/business"

# define a function to scrape the news from a given URL
def scrape_news(url: str):

    # send a GET request to the URL
    response = requests.get(url)

    # parse the HTML content of the response
    soup = BeautifulSoup(response.content, "html.parser")

    # extract the titles, bodies, dates, and summaries of the news articles
    titles = soup.find_all("h2", class_="title")
    print(titles)
    bodies = soup.find_all("p", class_="summary")
    dates = soup.find_all("time", class_="date")
    summaries = soup.find_all("p", class_="summary")

    # print the titles, bodies, dates, and summaries
    for title, body, date, summary in zip(titles, bodies, dates, summaries):
        print(title.text)
        print(body.text)
        print(date.text)
        print(summary.text)


# scrape the news from each of the websites
# scrape_news(nyt_url, "sdkjfh")
# scrape_news(economist_url, "dfkjdj")
# scrape_news(wsj_url)
# scrape_news(ft_url)


# Text as data workshop / text as data / in economics /
# Twitter APi
