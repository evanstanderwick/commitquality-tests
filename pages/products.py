"""
This module contains ProductsPage,
the page object for commitquality.com/
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class ProductsPage:

    # URL
    URL = "https://commitquality.com"


    # Locators
    PRODUCTS_LINK = (By.CSS_SELECTOR, '[data-testid="navbar-products"]')

    ADD_PRODUCT_LINK = (By.CSS_SELECTOR, '[data-testid="navbar-addproduct"]')

    PRACTICE_LINK = (By.CSS_SELECTOR, '[data-testid="navbar-practice"]')

    LEARN_LINK = (By.CSS_SELECTOR, '[data-testid="navbar-learn"]')

    LOGIN_LINK = (By.CSS_SELECTOR, '[data-testid="navbar-login"]')

    FILTER_BUTTON = (By.CSS_SELECTOR, '[data-testid="filter-button"]')

    RESET_BUTTON = (By.CSS_SELECTOR, '[data-testid="reset-filter-button"]')

    SHOW_MORE_BUTTON = (By.CSS_SELECTOR, '[data-testid="show-more-button"]')

    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, '[data-testid="add-a-product-button"]')

    PRODUCTS_TABLE_ROWS = (By.CSS_SELECTOR, 'tr')

    PRODUCTS_NAMES = (By.CSS_SELECTOR, '[data-testid="name"]')

    FILTER_FIELD = (By.CLASS_NAME, 'filter-textbox')

    ADD_PRODUCT_MESSAGE = (By.CLASS_NAME, 'add-product-message')


    # Initializer
    def __init__(self, browser):
        self.browser = browser


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


    def switch_window(self, window_index: int):
        self.browser.switch_to.window(self.browser.window_handles[window_index])


    def get_products_table_rows(self):
        return self.browser.find_elements(*ProductsPage.PRODUCTS_TABLE_ROWS)
    

    def get_products_names(self):
        """
        Returns:
        str[]: list of product names in the products table
        """

        names = []

        name_columns = self.browser.find_elements(*ProductsPage.PRODUCTS_NAMES)
        for column in name_columns:
            names.append(column.text)

        return names
    

    def type_filter_field(self, input: str):
        filter_field = self.browser.find_element(*ProductsPage.FILTER_FIELD)
        filter_field.send_keys(input)


    def get_product_message_text(self):
        return self.browser.find_element(*ProductsPage.ADD_PRODUCT_MESSAGE).text
    

    def get_filter_field_text(self):
        return self.browser.find_element(*ProductsPage.FILTER_FIELD).text


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
