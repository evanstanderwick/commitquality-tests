"""
Tests for commitquality.com/
"""

#
# imports
#

from pages.products import ProductsPage
import pytest
from selenium.webdriver.support.color import Color


# tests

def test_hover_products_link(products_page):
    # Given commitquality.com

    # When the cursor hovers over the products link
    products_link = products_page.hover(ProductsPage.PRODUCTS_LINK)

    # Then the products link is underlined
    assert products_link.value_of_css_property("text-decoration-line") == "underline"


@pytest.mark.parametrize('locator',
                         [ProductsPage.ADD_PRODUCT_LINK,
                          ProductsPage.PRACTICE_LINK,
                          ProductsPage.LEARN_LINK,
                          ProductsPage.LOGIN_LINK,
                          ])
def test_hover_nonproducts_link(products_page, locator):
    # Given commitquality.com

    # When the cursor hovers over the link
    link = products_page.hover(locator)

    # Then the link is underlined
    assert link.value_of_css_property("text-decoration-line") == "underline"

    # And the link is yellow
    assert Color.from_string(link.value_of_css_property("color")).hex == "#ffdf6b"


@pytest.mark.parametrize('locator', [ProductsPage.FILTER_BUTTON,
                                     ProductsPage.RESET_BUTTON,
                                     ProductsPage.SHOW_MORE_BUTTON,
                                     ProductsPage.ADD_PRODUCT_BUTTON])
def test_hover_buttons(products_page, locator):
    # Given commitquality.com

    # When the cursor hovers over the button
    button = products_page.hover(locator)

    # Then the button is white
    assert Color.from_string(button.value_of_css_property("background-color")).hex == "#ffffff"

    # And the text is black
    assert Color.from_string(button.value_of_css_property("color")).hex == "#333333"


@pytest.mark.parametrize("locator,url", [(ProductsPage.PRODUCTS_LINK, "https://commitquality.com/"),
                                     (ProductsPage.ADD_PRODUCT_LINK, "https://commitquality.com/add-product"),
                                     (ProductsPage.PRACTICE_LINK, "https://commitquality.com/practice"),
                                     (ProductsPage.LOGIN_LINK, "https://commitquality.com/login"),
                                     (ProductsPage.ADD_PRODUCT_BUTTON, "https://commitquality.com/add-product")])
def test_click_links(products_page, locator, url):
    # Given commitquality.com

    # When you click a link
    products_page.click(locator)

    # Then you'll be taken to the correct url in the current window
    assert products_page.current_url() == url


def test_click_learn_link(products_page):
    # Given commitquality.com

    # When you click the learn link
    products_page.click(ProductsPage.LEARN_LINK)

    # Then your browser will open a new tab at youtube.com/@commitquality
    products_page.switch_window(1)
    assert products_page.current_url() == "https://www.youtube.com/@commitquality"


def test_click_filter_button_no_text(products_page):
    num_rows_before = len(products_page.get_products_table_rows())

    # Given commitquality.com

    # Given the filter field is empty

    # When you click the filter button
    products_page.click(ProductsPage.FILTER_BUTTON)

    # Then the products table will be unaffected
    num_rows_after = len(products_page.get_products_table_rows())
    assert num_rows_before == num_rows_after


def test_click_filter_button_no_matches(products_page):
    # Given commitquality.com

    # Given the filter field matches no items in the table
    products_page.type_filter_field("test")

    # When you click the filter button
    products_page.click(ProductsPage.FILTER_BUTTON)

    # Then no table will be displayed
    assert (products_page.exists(ProductsPage.PRODUCTS_TABLE_ROWS) == False)

    # And "No products found" is shown
    assert products_page.get_product_message_text() == "No products found"


@pytest.mark.parametrize("filter_string", ["product 1", "product"])
def test_click_filter_button_matches(products_page,filter_string):
    # Given commitquality.com

    # Given the filter string matches items in the table
    products_page.type_filter_field(filter_string)

    # When you click the filter button
    products_page.click(ProductsPage.FILTER_BUTTON)

    # Then all table entries' names start with the filter string
    names = products_page.get_products_names()
    for name in names:
        assert(name.lower().startswith(filter_string))


def test_click_reset_button_no_text_unfiltered(products_page):
    num_rows_before = len(products_page.get_products_table_rows())

    # Given commitquality.com

    # Given the filter field is empty

    # Given the table hasn't been filtered

    # When you click the reset button
    products_page.click(ProductsPage.RESET_BUTTON)

    # Then the products table will be unaffected
    num_rows_after = len(products_page.get_products_table_rows())
    assert num_rows_before == num_rows_after


def test_click_reset_button_has_text_unfiltered(products_page):
    # Given commitquality.com

    # Given the filter field has text
    products_page.type_filter_field("test")

    # Given the table hasn't been filtered

    # When you click the reset button
    products_page.click(ProductsPage.RESET_BUTTON)

    # Then the filter field will be empty
    assert products_page.get_filter_field_text() == ""


def test_click_reset_button_has_text_filtered(products_page):
    num_rows_before = len(products_page.get_products_table_rows())

    # Given commitquality.com

    # Given the filter field has text
    products_page.type_filter_field("test")

    # Given the table has been filtered
    products_page.click(ProductsPage.FILTER_BUTTON)

    # When you click the reset button
    products_page.click(ProductsPage.RESET_BUTTON)

    # Then the filter field will be empty
    assert products_page.get_filter_field_text() == ""

    # And the products table will return to its original state
    num_rows_after = len(products_page.get_products_table_rows())
    assert num_rows_before == num_rows_after


def test_click_show_more_button(products_page):
    # Given commitquality.com

    # When you click the Show More buttonself
    products_page.click(ProductsPage.SHOW_MORE_BUTTON)

    # Then the show more button disappears
    assert (products_page.exists(ProductsPage.SHOW_MORE_BUTTON) == False)

    # And 11 or more products display
    assert len(products_page.get_products_table_rows()) >= 12 # 11 rows for products, 1 row for the header


def test_tab_order(products_page):
    # Given commitquality.com

    # When you tab through all elements on the pages
    # Then the elements will be focused upon in the correct order
    tab_order = [ProductsPage.PRODUCTS_LINK,
                 ProductsPage.ADD_PRODUCT_LINK,
                 ProductsPage.PRACTICE_LINK,
                 ProductsPage.LEARN_LINK,
                 ProductsPage.LOGIN_LINK,
                 ProductsPage.FILTER_FIELD,
                 ProductsPage.FILTER_BUTTON,
                 ProductsPage.RESET_BUTTON,
                 ProductsPage.SHOW_MORE_BUTTON,
                 ProductsPage.ADD_PRODUCT_BUTTON]
    
    for i in range(len(tab_order)):
        products_page.tab_to_next_element()
        focused_element = products_page.get_focused_element()
        assert focused_element == products_page.get_element(tab_order[i])