"""
Fixtures
"""

import pytest
import selenium.webdriver
import json
from pages.products import ProductsPage


@pytest.fixture
def browser():
    b = selenium.webdriver.Chrome()
    b.implicitly_wait(10)

    yield b

    b.quit()


@pytest.fixture
def products_page(browser):
    products_page = ProductsPage(browser)
    products_page.load()
    return products_page