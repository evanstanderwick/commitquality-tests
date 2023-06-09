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


    def current_url(self) -> str:
        return self.browser.current_url
    

    def get_element(self, locator):
        return self.browser.find_element(*locator)


    # locator: one of the locator ProductsPage class attributes
    def hover(self, locator):
        element = self.get_element(locator)
        hover = ActionChains(self.browser).move_to_element(element)
        hover.perform()
        return element
    

    # locator: one of the locator ProductsPage class attributes
    def click(self, locator):
        element = self.get_element(locator)
        element.click()


    def exists(self, locator) -> bool:
        raw_css_selector = locator[1]
        if raw_css_selector[0]=="[":
            raw_css_selector = raw_css_selector[1:len(locator[1]) - 1]
        return raw_css_selector in self.browser.page_source
    
    
    def get_focused_element(self):
        return self.browser.switch_to.active_element


    def tab_to_next_element(self):
        self.get_focused_element().send_keys(Keys.TAB)


    def switch_window(self, window_index: int):
        self.browser.switch_to.window(self.browser.window_handles[window_index])


    def type_field(self, input: str, locator):
        field = self.get_element(locator)
        field.send_keys(input)


    def get_field_text(self, locator):
        field = self.get_element(locator)
        return field.get_attribute("value")
    

    def refresh(self):
        self.browser.refresh()