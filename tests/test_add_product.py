"""
Tests for commitquality.com/add-product
"""

# 
# imports
# 

from pages.add_product import AddProductPage
from pages.products import ProductsPage
import pytest
from selenium.webdriver.support.color import Color


# 
# tests
# 

def test_hover_add_product_link(add_product_page):
    # Given commitquality.com/add-product

    # When the cursor hovers over the add product link
    add_products_link = add_product_page.hover(AddProductPage.ADD_PRODUCT_LINK)

    # Then the add product link is underlined
    assert add_products_link.value_of_css_property("text-decoration-line") == "underline"


@pytest.mark.parametrize('locator',
                         [AddProductPage.PRODUCTS_LINK,
                          AddProductPage.PRACTICE_LINK,
                          AddProductPage.LEARN_LINK,
                          AddProductPage.LOGIN_LINK,
                          ])
def test_hover_nonadd_product_link(add_product_page, locator):
    # Given commitquality.com/add-product

    # When the cursor hovers over the link
    link = add_product_page.hover(locator)

    # Then the link is underlined
    assert link.value_of_css_property("text-decoration-line") == "underline"

    # And the link is yellow
    assert Color.from_string(link.value_of_css_property("color")).hex == "#ffdf6b"


def test_hover_submit_button(add_product_page):
    # Given commitquality.com/add-product

    # When the cursor hovers over the submit button
    button = add_product_page.hover(AddProductPage.SUBMIT_BUTTON)

    # Then the button is white
    assert Color.from_string(button.value_of_css_property("background-color")).hex == "#ffffff"

    # And the text is black
    assert Color.from_string(button.value_of_css_property("color")).hex == "#333333"


def test_hover_cancel_button(add_product_page):
    # Given commitquality.com/add-product

    # When the cursor hovers over the cancel button
    cancel_button = add_product_page.hover(AddProductPage.CANCEL_BUTTON)

    # Then the text is underlined
    assert cancel_button.value_of_css_property("text-decoration-line") == "underline"


@pytest.mark.parametrize("locator,url", [(AddProductPage.PRODUCTS_LINK, "https://commitquality.com/"),
                                     (AddProductPage.ADD_PRODUCT_LINK, "https://commitquality.com/add-product"),
                                     (AddProductPage.PRACTICE_LINK, "https://commitquality.com/practice"),
                                     (AddProductPage.LOGIN_LINK, "https://commitquality.com/login")])
def test_click_links(add_product_page, locator, url):
    # Given commitquality.com/add-product

    # When you click a link
    add_product_page.click(locator)

    # Then you'll be taken to the correct url in the current window
    assert add_product_page.current_url() == url


def test_click_learn_link(add_product_page):
    # Given commitquality.com/add-product

    # When you click the learn link
    add_product_page.click(AddProductPage.LEARN_LINK)

    # Then your browser will open a new tab at youtube.com/@commitquality
    add_product_page.switch_window(1)
    assert add_product_page.current_url() == "https://www.youtube.com/@commitquality"


def test_click_submit_button_no_input(add_product_page):
    # Given commitquality.com/add-product

    # Given no fields have input

    # When you click the submit button
    add_product_page.click(AddProductPage.SUBMIT_BUTTON)

    # Then this error will appear above the name field: “Name must be at least 2 characters."
    text = add_product_page.get_div_after_element(AddProductPage.NAME_LABEL).text
    assert text == "Name must be at least 2 characters."

    # And this error will appear above the price field: "Price must not be empty and within 10 digits"
    text = add_product_page.get_div_after_element(AddProductPage.PRICE_LABEL).text
    assert text == "Price must not be empty and within 10 digits"

    # And this error will appear above the date field: "Date must not be empty."
    text = add_product_page.get_div_after_element(AddProductPage.DATE_LABEL).text
    assert text == "Date must not be empty."

    # And this error will appear below the date field: "Please fill in all fields"
    text = add_product_page.get_fillin_all_fields_validation_text()
    assert text == "Please fill in all fields"

    # And this error will appear above the submit/cancel buttons: "Errors must be resolved before submitting"
    text = add_product_page.get_all_fields_validation_text()
    assert text == "Errors must be resolved before submitting"


def test_click_submit_button_no_name_input(add_product_page):
    # Given commitquality.com/add-product

    # Given only the price and date fields have input
    add_product_page.type_field("5", AddProductPage.PRICE_FIELD)
    add_product_page.type_field("01012020", AddProductPage.DATE_FIELD)

    # When you click the submit button
    add_product_page.click(AddProductPage.SUBMIT_BUTTON)

    # Then this error will appear above the name field: “Name must be at least 2 characters."
    text = add_product_page.get_div_after_element(AddProductPage.NAME_LABEL).text
    assert text == "Name must be at least 2 characters."

    # And this error will appear below the date field: "Please fill in all fields"
    text = add_product_page.get_fillin_all_fields_validation_text()
    assert text == "Please fill in all fields"

    # And this error will appear above the submit/cancel buttons: "Errors must be resolved before submitting"
    text = add_product_page.get_all_fields_validation_text()
    assert text == "Errors must be resolved before submitting"


def test_click_submit_button_no_price_input(add_product_page):
    # Given commitquality.com/add-product

    # Given only the name and date fields have input
    add_product_page.type_field("test", AddProductPage.NAME_FIELD)
    add_product_page.type_field("01012020", AddProductPage.DATE_FIELD)

    # When you click the submit button
    add_product_page.click(AddProductPage.SUBMIT_BUTTON)

    # Then this error will appear above the price field: "Price must not be empty and within 10 digits"
    text = add_product_page.get_div_after_element(AddProductPage.PRICE_LABEL).text
    assert text == "Price must not be empty and within 10 digits"

    # And this error will appear below the date field: "Please fill in all fields"
    text = add_product_page.get_fillin_all_fields_validation_text()
    assert text == "Please fill in all fields"

    # And this error will appear above the submit/cancel buttons: "Errors must be resolved before submitting"
    text = add_product_page.get_all_fields_validation_text()
    assert text == "Errors must be resolved before submitting"


def test_click_submit_button_no_date_input(add_product_page):
    # Given commitquality.com/add-product

    # Given only the name and price fields have input
    add_product_page.type_field("test", AddProductPage.NAME_FIELD)
    add_product_page.type_field("5", AddProductPage.PRICE_FIELD)

    # When you click the submit button
    add_product_page.click(AddProductPage.SUBMIT_BUTTON)

    # Then this error will appear above the date field: "Date must not be empty."
    text = add_product_page.get_div_after_element(AddProductPage.DATE_LABEL).text
    assert text == "Date must not be empty."

    # And this error will appear below the date field: "Please fill in all fields"
    text = add_product_page.get_fillin_all_fields_validation_text()
    assert text == "Please fill in all fields"

    # And this error will appear above the submit/cancel buttons: "Errors must be resolved before submitting"
    text = add_product_page.get_all_fields_validation_text()
    assert text == "Errors must be resolved before submitting"


def test_click_submit_button_name_input_1_char(add_product_page):
    # Given commitquality.com/add-product

    # Given the price and date fields have input
    add_product_page.type_field("5", AddProductPage.PRICE_FIELD)
    add_product_page.type_field("01012020", AddProductPage.DATE_FIELD)

    # Given the name field has only 1 character input
    add_product_page.type_field("t", AddProductPage.NAME_FIELD)

    # When you click the submit button
    add_product_page.click(AddProductPage.SUBMIT_BUTTON)

    # Then this error will appear above the name field: "Name must be at least 2 characters."
    text = add_product_page.get_div_after_element(AddProductPage.NAME_LABEL).text
    assert text == "Name must be at least 2 characters."

    # And this error will appear above the submit/cancel buttons: "Errors must be resolved before submitting"
    text = add_product_page.get_all_fields_validation_text()
    assert text == "Errors must be resolved before submitting"


def test_click_submit_button_name_input_2_chars(products_page, add_product_page):
    # Given commitquality.com/add-product

    # Given the price and date fields have input
    add_product_page.type_field("5", AddProductPage.PRICE_FIELD)
    add_product_page.type_field("01012020", AddProductPage.DATE_FIELD)

    # Given the name field has 2 characters input
    add_product_page.type_field("te", AddProductPage.NAME_FIELD)

    # When you click the submit button
    add_product_page.click(AddProductPage.SUBMIT_BUTTON)

    # Then you will be taken to commitquality.com/
    assert add_product_page.current_url() == ProductsPage.URL

    # And the product you added will be at the top of the products table
    row_data = products_page.get_products_table_first_product_data()

    # row_data[0] is id
    assert row_data[1].text == "te"
    assert row_data[2].text == "5"
    assert row_data[3].text == "2020-01-01"


def test_click_submit_button_name_input_5_chars(products_page, add_product_page):
    # Given commitquality.com/add-product

    # Given the price and date fields have input
    add_product_page.type_field("5", AddProductPage.PRICE_FIELD)
    add_product_page.type_field("01012020", AddProductPage.DATE_FIELD)

    # Given the name field has 5 characters input
    add_product_page.type_field("testo", AddProductPage.NAME_FIELD)

    # When you click the submit button
    add_product_page.click(AddProductPage.SUBMIT_BUTTON)

    # Then you will be taken to commitquality.com/
    assert add_product_page.current_url() == ProductsPage.URL

    # And the product you added will be at the top of the products table
    row_data = products_page.get_products_table_first_product_data()

    # row_data[0] is id
    assert row_data[1].text == "testo"
    assert row_data[2].text == "5"
    assert row_data[3].text == "2020-01-01"


def test_click_submit_button_price_input_11_chars(add_product_page):
    # Given commitquality.com/add-product

    # Given the name and date fields have input
    add_product_page.type_field("testo", AddProductPage.NAME_FIELD)
    add_product_page.type_field("01012020", AddProductPage.DATE_FIELD)

    # Given the price field has 11 characters input
    add_product_page.type_field("12345678901", AddProductPage.PRICE_FIELD)

    # When you click the submit button
    add_product_page.click(AddProductPage.SUBMIT_BUTTON)

    # Then this error will appear above the price field: "Price must not be empty and within 10 digits"
    text = add_product_page.get_div_after_element(AddProductPage.PRICE_LABEL).text
    assert text == "Price must not be empty and within 10 digits"

    # And this error will appear above the submit/cancel buttons: "Errors must be resolved before submitting"
    text = add_product_page.get_all_fields_validation_text()
    assert text == "Errors must be resolved before submitting"