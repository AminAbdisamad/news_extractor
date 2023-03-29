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


# testing_data = [
#     {
#         "title": "US targets Iran 'shadow banking', drone network in new sanctions",
#         "date": "MAR 09, 2023",
#         "url": "https://www.dailysabah.com/business/economy/us-targets-iran-shadow-banking-drone-network-in-new-sanctions",
#     },
#     {
#         "title": "Biden pitches budget with higher taxes on rich, sets up 2024 run",
#         "date": "MAR 09, 2023",
#         "url": "https://www.dailysabah.com/business/economy/biden-pitches-budget-with-higher-taxes-on-rich-sets-up-2024-run",
#     },
#     {
#         "title": "Russia says extending Ukraine grain deal 'complicated'",
#         "date": "MAR 09, 2023",
#         "url": "https://www.dailysabah.com/business/economy/russia-says-extending-ukraine-grain-deal-complicated",
#     },
#     {
#         "title": "Türkiye's exports to Saudi Arabia surges 30-fold in Jan-Feb",
#         "date": "MAR 09, 2023",
#         "url": "https://www.dailysabah.com/business/economy/turkiyes-exports-to-saudi-arabia-surges-30-fold-in-jan-feb",
#     },
#     {
#         "title": "European bank to invest up to $1.6B in Türkiye's quake-hit region",
#         "date": "MAR 09, 2023",
#         "url": "https://www.dailysabah.com/business/economy/european-bank-to-invest-up-to-16b-in-turkiyes-quake-hit-region",
#     },
#     {
#         "title": "Halkbank unveils financing for women entrepreneurs in Türkiye's quake zone",
#         "date": "MAR 08, 2023",
#         "url": "https://www.dailysabah.com/business/economy/halkbank-unveils-financing-for-women-entrepreneurs-in-turkiyes-quake-zone",
#     },
#     {
#         "title": "Turkish agricultural sector logs highest Jan-Feb exports",
#         "date": "MAR 08, 2023",
#         "url": "https://www.dailysabah.com/business/economy/turkish-agricultural-sector-logs-highest-jan-feb-exports",
#     },
# ]


def save_csv(articles):
    with open(
        "corpus/daily_sabah_summary.csv", mode="a", encoding="utf-8", newline=""
    ) as f:
        fieldnames = ["date", "title", "url"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for article in articles:
            print("inside csv", article)
            writer.writerow(article)


btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (
            By.CSS_SELECTOR,
            "a[data-view='ajax_section_articles']",
        )
    )
)


# Scroll to the button's location


# # Click the button using JavaScript
# driver.execute_script("arguments[0].click();", btn)

current_count = 9
while btn is not None:
    # driver.execute_script("arguments[0].scrollIntoView();", btn)
    # Click the button using JavaScript
    driver.execute_script("arguments[0].click();", btn)

    try:
        # Wait for new articles to be loaded
        data = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "ul"))
        )
        articles = extract(data)

        save_csv(articles)
        print("Saving article", articles)

        # Find the new button to click
        # [data-section_articles="13"]"
        btn = driver.find_element(
            By.CSS_SELECTOR,
            f"a[data-view='ajax_section_articles'][data-llmit_articles='100'][data-current_count='{current_count}']",
        )

    except:
        # If no new button is found, set button to None to exit the loop
        button = None


# # Create function that saves the data to a csv file

driver.quit()
