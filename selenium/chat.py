from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

driver = webdriver.Chrome()
driver.maximize_window()

website = "https://www.dailysabah.com/economy"
driver.get(website)

# Wait for the initial load of articles
articles = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div#ajax_section_articles ul.items_list li")
    )
)


def extract_article_data(article):
    link = article.find_element(By.TAG_NAME, "a")
    title = article.text.split("\n")[0]
    date = article.text.split("\n")[1]
    url = link.get_attribute("href")
    return {"title": title, "date": date, "url": url}


def extract_articles(elements):
    return [extract_article_data(el) for el in elements]


def save_articles_to_csv(articles, filename):
    with open(filename, mode="a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "date", "url"])
        writer.writerows(articles)


# Extract and save the initial batch of articles
articles_data = extract_articles(articles)
save_articles_to_csv(articles_data, "corpus/daily_sabah_summary.csv")

# Get the last article on the page
last_article = articles[-1]

# Keep scrolling and loading more articles until there are no more
while True:
    try:
        # Find and click the "load more" button
        btn = driver.find_element(
            By.CSS_SELECTOR,
            "a[data-view='ajax_section_articles'][data-llmit_articles='100']",
        )
        driver.execute_script("arguments[0].scrollIntoView();", btn)
        driver.execute_script("arguments[0].click();", btn)

        # Wait for new articles to load
        new_articles = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div#ajax_section_articles ul.items_list li")
            )
        )

        # Extract and save the new articles
        new_articles_data = extract_articles(new_articles)
        save_articles_to_csv(new_articles_data, "corpus/daily_sabah_summary.csv")

        # If the last article is still present, set it to be the new last article
        if last_article in new_articles:
            last_article = new_articles[-1]
        # Otherwise, we've reached the end of the articles and can stop scrolling
        else:
            break

    except Exception as e:
        print("Error: ", e)
        break

driver.quit()
