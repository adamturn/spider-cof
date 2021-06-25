import random

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumSpider:
    def __init__(self, driver: webdriver.Chrome, max_timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, random.randint(10, max_timeout))

    @classmethod
    def construct(cls, headless: bool, user_agent: str, exe_path: str):
        opts = webdriver.ChromeOptions()
        if headless:
            opts.headless = True

        driver = webdriver.Chrome(
            chrome_options=opts,
            service=webdriver.chrome.service.Service(executable_path=exe_path)
        )
        driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": user_agent})

        return cls(driver)

    def wait_until_clickable(self, xpath):
        self.wait.until(expected_conditions.element_to_be_clickable((webdriver.common.by.By.XPATH, xpath)))

        return None

    def wait_until_invisible(self, xpath):
        self.wait.until(expected_conditions.invisibility_of_element_located((webdriver.common.by.By.XPATH, xpath)))

        return None

    def wait_until_visible(self, xpath):
        self.wait.until(expected_conditions.visibility_of_element_located((webdriver.common.by.By.XPATH, xpath)))

        return None

    def execute_click_script(self, xpath):
        self.driver.execute_script(
            "arguments[0].click();", 
            self.wait.until(expected_conditions.element_to_be_clickable((webdriver.common.by.By.XPATH, xpath)))
        )

        return None


class Pipeline:
    def __init__(self, bot, cfg):
        self.bot = bot
        self.cfg = cfg
