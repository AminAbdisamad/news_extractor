import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Set the start and end dates for scraping
start_date = datetime(2015, 1, 1)
end_date = datetime.now()

# Create a CSV file to save the results
with open(
    "dailysabah_economy_news.csv", mode="w", encoding="utf-8", newline=""
) as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Date", "Body"])

    # Loop through each day between the start and end dates
    current_date = start_date
    while current_date <= end_date:
        # Build the URL for the day's news
        url = "https://www.dailysabah.com/economy/" + current_date.strftime("%Y-%m-%d")
        print("Scraping URL ", url)
        # Send a request to the URL and parse the response with Beautiful Soup
        response = requests.get(url)
        print("response status", response.status_code)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all the news articles on the page
        articles = soup.find_all("div", {"class": "newsBox"})

        # Loop through each article and extract the title, date, and body
        for article in articles:
            title = article.find("h3", {"class": "newsTitle"}).text.strip()
            date = article.find("div", {"class": "newsDate"}).text.strip()
            body = article.find("div", {"class": "newsSummary"}).text.strip()

            # Write the results to the CSV file
            writer.writerow([title, date, body])

        # Move to the next day
        current_date += timedelta(days=1)

print("Scraping complete.")
