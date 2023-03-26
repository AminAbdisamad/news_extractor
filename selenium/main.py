from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint

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
                title = article.text.split("\n")[0]
                date = article.text.split("\n")[1]
                found_articles.append({"title": title, "date": date})
            break
    return found_articles


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

while btn is not None and len(unique_articles) < 100:
    # Click the button using JavaScript
    driver.execute_script("arguments[0].click();", btn)

    try:
        # Wait for new articles to be loaded
        data = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "ul"))
        )
        articles = extract(data)
        pprint(articles)

        # Find the new button to click
        btn = driver.find_element(
            By.CSS_SELECTOR,
            "a[data-view='ajax_section_articles'][data-llmit_articles='100']",
        )

    except:
        # If no new button is found, set button to None to exit the loop
        button = None


driver.quit()
