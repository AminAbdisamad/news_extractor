from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import WebDriverWait


driver = webdriver.Chrome()
print("Chrome driver is ready to use")
website = driver.get("https://www.dailysabah.com/economy")
print("Website is opened")
driver.maximize_window()
print("Window is maximized")
driver.implicitly_wait(0.5)
print("Implicit wait is applied")


# [{title:"some title", date:"some date"}]


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


# elements = driver.find_elements(By.TAG_NAME, "ul")
# articles = extract(elements)

# Load more button

# load_more_button = driver.find_element(By.CLASS_NAME, "loadMoreArticleButton")
# load_more_button = driver.find_element(
#     By.XPATH, "/html/body/section/div[2]/div[4]/div[1]/div/div[4]/a"
# )

loadingButton = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "/html/body/section/div[2]/div[4]/div[1]/div/div[4]/a")
    )
)

# driver.implicitly_wait(15)
# load_more_button.click()
# driver.implicitly_wait(15)
# print(load_more_button)

# elements = driver.find_elements(By.TAG_NAME, "ul")
# articles += extract(elements)


# print("Number of articles: ", len(articles))
# print(articles)


# click = ActionChains(driver).click(load_more_button).perform()
# driver.implicitly_wait(15)
# time.sleep(2)
# print(click)

driver.quit()
