from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint
import csv

# import WebDriverWait


driver = webdriver.Chrome()
print("Chrome driver is ready to use")
website = driver.get("https://www.dailysabah.com/economy")
print("Website is opened")
driver.maximize_window()
print("Window is maximized")
driver.implicitly_wait(0.5)
print("Implicit wait is applied")


def extract(elements):
    found_articles = []
    for el in elements:
        if el.get_attribute("class") == "items_list":
            articels = el.find_elements(By.TAG_NAME, "li")
            for article in articels:
                link = article.find_element(By.TAG_NAME, "a")
                title = article.text.split("\n")[0]
                date = article.text.split("\n")[1]
                found_articles.append(
                    {"title": title, "date": date, "url": link.get_attribute("href")}
                )
            break
    return found_articles


def save_csv(articles):
    with open(
        "corpus/daily_sabah_summary.csv", mode="a", encoding="utf-8", newline=""
    ) as f:
        fieldnames = ["title", "date", "url"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for article in articles:
            print("inside csv", article)
            writer.writerow(article)


btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "a[data-view='ajax_section_articles']")
    )
)

unique_articles = set()


# Scroll to the button's location
driver.execute_script("arguments[0].scrollIntoView();", btn)

# # Click the button using JavaScript
driver.execute_script("arguments[0].click();", btn)

while btn is not None:
    # Click the button using JavaScript
    driver.execute_script("arguments[0].click();", btn)

    try:
        # Wait for new articles to be loaded
        data = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "ul"))
        )
        articles = extract(data)
        # save_csv(articles)

        # Find the new button to click
        btn = driver.find_element(
            By.CSS_SELECTOR,
            "a[data-view='ajax_section_articles'][data-llmit_articles='100']",
        )

    except:
        # If no new button is found, set button to None to exit the loop
        button = None


# Create function that saves the data to a csv file

driver.quit()
