"""
This module contains AddProductPage,
the page object for commitquality.com/add-product
"""

from selenium.webdriver.common.by import By

class AddProductPage:
    # URL
    URL = "https://commitquality.com/add-product"

    # Locators
    PRODUCTS_LINK = (By.CSS_SELECTOR, '[data-testid="navbar-products"]')

    ADD_PRODUCT_LINK = (By.CSS_SELECTOR, '[data-testid="navbar-addproduct"]')

    PRACTICE_LINK = (By.CSS_SELECTOR, '[data-testid="navbar-practice"]')

    LEARN_LINK = (By.CSS_SELECTOR, '[data-testid="navbar-learn"]')

    LOGIN_LINK = (By.CSS_SELECTOR, '[data-testid="navbar-login"]')

    NAME_FIELD = (By.CSS_SELECTOR, '[data-testid="product-textbox"]')

    PRICE_FIELD = (By.CSS_SELECTOR, '[data-testid="price-textbox"]')

    DATE_FIELD = (By.CSS_SELECTOR, '[data-testid="date-stocked"]')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[data-testid="submit-form"]')

    CANCEL_BUTTON = (By.CSS_SELECTOR, '[data-testid="cancel-button"]')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)