"""
This module contains AddProductPage,
the page object for commitquality.com/add-product
"""

from selenium.webdriver.common.by import By
from pages.generic_page import GenericPage

class AddProductPage(GenericPage):

    # URL
    URL = "https://commitquality.com/add-product"


    # Locators
    NAME_LABEL = (By.CSS_SELECTOR, '[for="name"]')

    PRICE_LABEL = (By.CSS_SELECTOR, '[for="price"]')

    DATE_LABEL = (By.CSS_SELECTOR, '[for="dateStocked"]')

    NAME_FIELD = (By.CSS_SELECTOR, '[data-testid="product-textbox"]')

    PRICE_FIELD = (By.CSS_SELECTOR, '[data-testid="price-textbox"]')

    DATE_FIELD = (By.CSS_SELECTOR, '[data-testid="date-stocked"]')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[data-testid="submit-form"]')

    CANCEL_BUTTON = (By.CSS_SELECTOR, '[data-testid="cancel-button"]')

    FILLIN_ALL_FIELDS_VALIDATION = (By.CSS_SELECTOR, '[data-testid="fillin-all-fields-validation"]')

    ALL_FIELDS_VALIDATION = (By.CSS_SELECTOR, '[data-testid="all-fields-validation"]')


    # Interaction Methods

    def get_div_after_element(self, locator):
        return self.browser.find_element(By.CSS_SELECTOR, locator[1] + '+div')
    

    def get_fillin_all_fields_validation_text(self):
        return self.browser.find_element(*AddProductPage.FILLIN_ALL_FIELDS_VALIDATION).text
    
    
    def get_all_fields_validation_text(self):
        return self.browser.find_element(*AddProductPage.ALL_FIELDS_VALIDATION).text