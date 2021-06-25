from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def login(bot: webdriver.Chrome, cfg: dict) -> None:
    bot.driver.get(cfg["extract"]["url"])
    login_xpath = "//*[@id='noAcctSubmit'"
    bot.driver.wait_until_clickable(login_xpath)
    username_box = bot.driver.find_element_by_xpath("//*[@aria-label='Username']")
    username_box.send_keys(cfg["auth"]["username"])
    password_box = bot.driver.find_element_by_xpath("//*[@aria-label='Password']")
    password_box.send_keys(cfg["auth"]["password"])
    password_box.send_keys(Keys.RETURN)


def load_historical_data(bot: webdriver.Chrome, cfg: dict, start_year: str) -> None:
    start_year_xpath = f"//*contains(text(), '{start_year} Transactions')]"
    more_data_xpath = "//*[contains(text(), 'View More Transactions')]"

    found_start = False
    while not found_start:
        bot.driver.find_element_by_xpath(more_data_xpath).click()
        bot.driver.wait_until_clickable(more_data_xpath)

        try:
            bot.driver.find_element_by_xpath(start_year_xpath)
        except:
            breakpoint()
            print("Could not find start year!")


def view_transaction_data(bot: webdriver.Chrome, cfg: dict) -> None:
    viewmore_xpath = "//*[@id='viewMore']"
    bot.driver.wait_until_clickable(viewmore_xpath)
    bot.driver.find_element_by_xpath(viewmore_xpath).click()

    load_historical_data(bot, cfg, )

# def extract_transaction_data(bot: webdriver.Chrome, cfg: dict) -> None:
