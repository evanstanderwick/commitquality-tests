"""
This module contains GenericPage,
a generic page object for commitquality.com
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class GenericPage:

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    
    # Navbar Locators
    
    PRODUCTS_LINK = (By.CSS_SELECTOR, '[data-testid="navbar-products"]')

    ADD_PRODUCT_LINK = (By.CSS_SELECTOR, '[data-testid="navbar-addproduct"]')

    PRACTICE_LINK = (By.CSS_SELECTOR, '[data-testid="navbar-practice"]')

    LEARN_LINK = (By.CSS_SELECTOR, '[data-testid="navbar-learn"]')

    LOGIN_LINK = (By.CSS_SELECTOR, '[data-testid="navbar-login"]')


    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)


    def current_url(self):
        return self.browser.current_url
    

    def get_element(self, locator):
        return self.browser.find_element(*locator)


    # locator: one of the locator ProductsPage class attributes
    def hover(self, locator):
        element = self.browser.find_element(*locator)
        hover = ActionChains(self.browser).move_to_element(element)
        hover.perform()
        return element
    

    # locator: one of the locator ProductsPage class attributes
    def click(self, locator):
        element = self.browser.find_element(*locator)
        element.click()


    def exists(self, locator):
        # TODO: this technically works, but waits the implicit wait amount before concluding that there are no table rows.
        # Update this to use driver.getPageSource() instead
        # https://www.tutorialspoint.com/how-do-i-verify-that-an-element-does-not-exist-in-selenium-2
        # https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/WebElement.html#findElements-org.openqa.selenium.By-
        elements = self.browser.find_elements(*locator)
        return (len(elements) != 0)
    
    
    def get_focused_element(self):
        return self.browser.switch_to.active_element


    def tab_to_next_element(self):
        self.get_focused_element().send_keys(Keys.TAB)


    def switch_window(self, window_index: int):
        self.browser.switch_to.window(self.browser.window_handles[window_index])


    def type_field(self, input: str, locator):
        field = self.browser.find_element(*locator)
        field.send_keys(input)