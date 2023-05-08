"""
This module contains ProductsPage,
the page object for commitquality.com/
"""

from pages.generic_page import GenericPage
from selenium.webdriver.common.by import By

class ProductsPage(GenericPage):

    # URL
    URL = "https://commitquality.com/"


    # Locators

    FILTER_BUTTON = (By.CSS_SELECTOR, '[data-testid="filter-button"]')

    RESET_BUTTON = (By.CSS_SELECTOR, '[data-testid="reset-filter-button"]')

    SHOW_MORE_BUTTON = (By.CSS_SELECTOR, '[data-testid="show-more-button"]')

    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, '[data-testid="add-a-product-button"]')

    PRODUCTS_TABLE_ROWS = (By.CSS_SELECTOR, 'tr')

    PRODUCTS_NAMES = (By.CSS_SELECTOR, '[data-testid="name"]')

    FILTER_FIELD = (By.CLASS_NAME, 'filter-textbox')

    ADD_PRODUCT_MESSAGE = (By.CLASS_NAME, 'add-product-message')


    # Interaction Methods

    def get_products_table_rows(self):
        # note: this includes the header row
        return self.browser.find_elements(*ProductsPage.PRODUCTS_TABLE_ROWS)


    def get_products_table_row_data(self, row_id):
        # Returns; (id, name, price, date stocked)
        # e.g. ("11", "Product 2", "15", "2021-02-01")
        data = []
        for i in range(1,5):
            data.append(self.browser.find_element(*(By.CSS_SELECTOR, '[data-testid="product-row-{row_id}"] td:nth-child({i})'.format(row_id=row_id,i=i))))
        return (*data,)


    def get_products_table_first_product_data(self):
        # Returns; (id, name, price, date stocked)
        # e.g. ("11", "Product 2", "15", "2021-02-01")
        data = []
        for i in range(1,5):
            data.append(self.browser.find_element(*(By.CSS_SELECTOR, 'tr td:nth-child({i})'.format(i=i))))
        return (*data,)
    

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


    def get_product_message_text(self):
        return self.browser.find_element(*ProductsPage.ADD_PRODUCT_MESSAGE).text
    

    def get_filter_field_text(self):
        return self.browser.find_element(*ProductsPage.FILTER_FIELD).text