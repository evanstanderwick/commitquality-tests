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


def test_click_submit_button_price_input_10_chars(products_page, add_product_page):
    # Given commitquality.com/add-product

    # Given the name and date fields have input
    add_product_page.type_field("testo", AddProductPage.NAME_FIELD)
    add_product_page.type_field("01012020", AddProductPage.DATE_FIELD)

    # Given the price field has 10 characters input
    add_product_page.type_field("1234567890", AddProductPage.PRICE_FIELD)

    # When you click the submit button
    add_product_page.click(AddProductPage.SUBMIT_BUTTON)

    # Then you will be taken to commitquality.com/
    assert add_product_page.current_url() == ProductsPage.URL

    # And the product you added will be at the top of the products table
    row_data = products_page.get_products_table_first_product_data()

    # row_data[0] is id
    assert row_data[1].text == "testo"
    assert row_data[2].text == "1234567890"
    assert row_data[3].text == "2020-01-01"


def test_click_submit_button_price_input_5_chars(products_page, add_product_page):
    # Given commitquality.com/add-product

    # Given the name and date fields have input
    add_product_page.type_field("testo", AddProductPage.NAME_FIELD)
    add_product_page.type_field("01012020", AddProductPage.DATE_FIELD)

    # Given the price field has 5 characters input
    add_product_page.type_field("12345", AddProductPage.PRICE_FIELD)

    # When you click the submit button
    add_product_page.click(AddProductPage.SUBMIT_BUTTON)

    # Then you will be taken to commitquality.com/
    assert add_product_page.current_url() == ProductsPage.URL

    # And the product you added will be at the top of the products table
    row_data = products_page.get_products_table_first_product_data()

    # row_data[0] is id
    assert row_data[1].text == "testo"
    assert row_data[2].text == "12345"
    assert row_data[3].text == "2020-01-01"


def test_click_submit_button_date_101_years_ago(add_product_page):
    # Given commitquality.com/add-product

    # Given the name and price fields have input
    add_product_page.type_field("testo", AddProductPage.NAME_FIELD)
    add_product_page.type_field("12345", AddProductPage.PRICE_FIELD)

    # Given the date field has a date 101 years ago
    date = AddProductPage.get_date_num_years_ago(101)
    add_product_page.type_field(date[1] + date[2] + date[0], AddProductPage.DATE_FIELD)

    # When you click the submit button
    add_product_page.click(AddProductPage.SUBMIT_BUTTON)

    # Then this error will appear above the date field: "Date must not be older than 100 years."
    text = add_product_page.get_div_after_element(AddProductPage.DATE_LABEL).text
    assert text == "Date must not be older than 100 years."

    # And this error will appear above the submit/cancel buttons: "Errors must be resolved before submitting"
    text = add_product_page.get_all_fields_validation_text()
    assert text == "Errors must be resolved before submitting"


def test_click_submit_button_date_100_years_ago(products_page, add_product_page):
    # Given commitquality.com/add-product

    # Given the name and price fields have input
    add_product_page.type_field("testo", AddProductPage.NAME_FIELD)
    add_product_page.type_field("12345", AddProductPage.PRICE_FIELD)

    # Given the date field has a date 100 years ago
    date = AddProductPage.get_date_num_years_ago(100)
    add_product_page.type_field(date[1] + date[2] + date[0], AddProductPage.DATE_FIELD)

    # When you click the submit button
    add_product_page.click(AddProductPage.SUBMIT_BUTTON)

    # Then you will be taken to commitquality.com/
    assert add_product_page.current_url() == ProductsPage.URL

    # And the product you added will be at the top of the products table
    row_data = products_page.get_products_table_first_product_data()

    # row_data[0] is id
    assert row_data[1].text == "testo"
    assert row_data[2].text == "12345"
    assert row_data[3].text == "{year}-{month}-{day}".format(year=date[0],month=date[1],day=date[2])


def test_click_submit_button_date_50_years_ago(products_page, add_product_page):
    # Given commitquality.com/add-product

    # Given the name and price fields have input
    add_product_page.type_field("testo", AddProductPage.NAME_FIELD)
    add_product_page.type_field("12345", AddProductPage.PRICE_FIELD)

    # Given the date field has a date 50 years ago
    date = AddProductPage.get_date_num_years_ago(50)
    add_product_page.type_field(date[1] + date[2] + date[0], AddProductPage.DATE_FIELD)

    # When you click the submit button
    add_product_page.click(AddProductPage.SUBMIT_BUTTON)

    # Then you will be taken to commitquality.com/
    assert add_product_page.current_url() == ProductsPage.URL

    # And the product you added will be at the top of the products table
    row_data = products_page.get_products_table_first_product_data()

    # row_data[0] is id
    assert row_data[1].text == "testo"
    assert row_data[2].text == "12345"
    assert row_data[3].text == "{year}-{month}-{day}".format(year=date[0],month=date[1],day=date[2])


def test_click_cancel_button_nothing_input(products_page, add_product_page):
    # Given commitquality.com/add-product

    # Given no fields have input

    # When you click the cancel button
    add_product_page.click(AddProductPage.CANCEL_BUTTON)

    # Then you will be taken to commitquality.com/
    assert add_product_page.current_url() == ProductsPage.URL

    # And all products visible in the table are named either Product 1 or Product 2
    num_rows = len(products_page.get_products_table_rows()) - 1 # -1 to account for header row
    first_row_id = int(products_page.get_products_table_first_product_data()[0].text)

    for id in range(first_row_id, first_row_id - num_rows, -1):
        row = products_page.get_products_table_row_data(id)
        name = row[1].text
        assert (
            (name == "Product 1") or (name == "Product 2")
        )


def test_click_cancel_button_everything_input(products_page, add_product_page):
    # Given commitquality.com/add-product

    # Given all fields have input
    add_product_page.type_field("testo", AddProductPage.NAME_FIELD)
    add_product_page.type_field("12345", AddProductPage.PRICE_FIELD)
    add_product_page.type_field("01012020", AddProductPage.DATE_FIELD)

    # When you click the cancel button
    add_product_page.click(AddProductPage.CANCEL_BUTTON)

    # Then you will be taken to commitquality.com/
    assert add_product_page.current_url() == ProductsPage.URL

    # And all products visible in the table are named either Product 1 or Product 2
    num_rows = len(products_page.get_products_table_rows()) - 1 # -1 to account for header row
    first_row_id = int(products_page.get_products_table_first_product_data()[0].text)

    for id in range(first_row_id, first_row_id - num_rows, -1):
        row = products_page.get_products_table_row_data(id)
        name = row[1].text
        assert (
            (name == "Product 1") or (name == "Product 2")
        )


def test_type_name_letters_numbers_symbols(add_product_page):
    # Given commitquality.com/add-product

    # When you type letters, numbers, and symbols in the name field
    input = "test123!"
    add_product_page.type_field(input, AddProductPage.NAME_FIELD)

    # Then the input you typed will appear in the name field
    assert add_product_page.get_field_text(AddProductPage.NAME_FIELD) == input


def test_type_price_numbers(add_product_page):
    # Given commitquality.com/add-product

    # When you type numbers in the price field
    input = "35"
    add_product_page.type_field(input, AddProductPage.PRICE_FIELD)

    # Then the input you typed will appear in the price field
    assert add_product_page.get_field_text(AddProductPage.PRICE_FIELD) == input


def test_type_price_letters_numbers_symbols(add_product_page):
    # Given commitquality.com/add-product

    # When you type letters numbers and symbols in the price field
    add_product_page.type_field("test -123!", AddProductPage.PRICE_FIELD)

    # Then only the numbers will appear in the price field
    assert add_product_page.get_field_text(AddProductPage.PRICE_FIELD) == "123"


def test_type_date_month_numbers(add_product_page):
    # Given commitquality.com/add-product

    # When you type a number in the date field
    input = "05162020"
    add_product_page.type_field(input, AddProductPage.DATE_FIELD)

    # Then the date field's value will be the input you typed
    assert add_product_page.get_field_text(AddProductPage.DATE_FIELD) == "2020-05-16"


def test_type_date_month_letters_numbers_symbols(add_product_page):
    # Given commitquality.com/add-product

    # When you type letters numbers and symbols in the date field
    input = "-05ab!16#A2020"
    add_product_page.type_field(input, AddProductPage.DATE_FIELD)

    # Then only the numbers will appear in the date field
    assert add_product_page.get_field_text(AddProductPage.DATE_FIELD) == "2020-05-16"


@pytest.mark.parametrize("name", ["","t"])
def test_tab_away_name_illegal(add_product_page,name):
    # Given commitquality.com/add-product

    # Given the name field has less than 2 characters input
    add_product_page.type_field(name, AddProductPage.NAME_FIELD)

    # When you tab away from the name field
    add_product_page.tab_to_next_element()

    # Then this error will appear above the name field: “Name must be at least 2 characters."
    text = add_product_page.get_div_after_element(AddProductPage.NAME_LABEL).text
    assert text == "Name must be at least 2 characters."

    # And this error will appear above the submit/cancel buttons: "Errors must be resolved before submitting"
    text = add_product_page.get_all_fields_validation_text()
    assert text == "Errors must be resolved before submitting"


@pytest.mark.parametrize("name", ["te","testo"])
def test_tab_away_name_legal(add_product_page,name):
    # Given commitquality.com/add-product

    # Given the name field has two or more characters input
    add_product_page.type_field(name, AddProductPage.NAME_FIELD)

    # When you tab away from the name field
    add_product_page.tab_to_next_element()

    # Then no errors appear on the page
    assert (add_product_page.errors_exist() == False)


@pytest.mark.parametrize("price", ["","12345678901"])
def test_tab_away_price_illegal(add_product_page,price):
    # Given commitquality.com/add-product

    # Given the price field has either 0 characters input or over 10 characters input
    add_product_page.type_field(price, AddProductPage.PRICE_FIELD)

    # When you tab away from the price field
    add_product_page.tab_to_next_element()

    # Then this error will appear above the price field: "Price must not be empty and within 10 digits"
    text = add_product_page.get_div_after_element(AddProductPage.PRICE_LABEL).text
    assert text == "Price must not be empty and within 10 digits"

    # And this error will appear above the submit/cancel buttons: "Errors must be resolved before submitting"
    text = add_product_page.get_all_fields_validation_text()
    assert text == "Errors must be resolved before submitting"


@pytest.mark.parametrize("price", ["1234567890","12345"])
def test_tab_away_price_legal(add_product_page,price):
    # Given commitquality.com/add-product

    # Given the price field has between [1,10] characters input
    add_product_page.type_field(price, AddProductPage.PRICE_FIELD)

    # When you tab away from the name field
    add_product_page.tab_to_next_element()

    # Then no errors appear on the page
    assert (add_product_page.errors_exist() == False)


def test_tab_away_date_no_input(add_product_page):
    # Given commitquality.com/add-product

    # Given the date field has no characters input
    add_product_page.type_field("", AddProductPage.DATE_FIELD)

    # When you tab away from the price field
    add_product_page.tab_to_next_element()
    add_product_page.tab_to_next_element()
    add_product_page.tab_to_next_element() # you need 3 here to get through the date input

    # Then this error will appear above the date field: "Date must not be empty."
    text = add_product_page.get_div_after_element(AddProductPage.DATE_LABEL).text
    assert text == "Date must not be empty."

    # And this error will appear above the submit/cancel buttons: "Errors must be resolved before submitting"
    text = add_product_page.get_all_fields_validation_text()
    assert text == "Errors must be resolved before submitting"


def test_tab_away_date_101_years_ago(add_product_page):
    # Given commitquality.com/add-product

    # Given the date field has the date from 101 years ago input
    date = AddProductPage.get_date_num_years_ago(101)
    add_product_page.type_field(date[1] + date[2] + date[0], AddProductPage.DATE_FIELD)

    # When you tab away from the date field
    add_product_page.tab_to_next_element()

    # Then this error will appear above the date field: "Date must not be older than 100 years."
    text = add_product_page.get_div_after_element(AddProductPage.DATE_LABEL).text
    assert text == "Date must not be older than 100 years."

    # And this error will appear above the submit/cancel buttons: "Errors must be resolved before submitting"
    text = add_product_page.get_all_fields_validation_text()
    assert text == "Errors must be resolved before submitting"


@pytest.mark.parametrize("years_ago", ["100","50"])
def test_tab_away_date_legal(add_product_page,years_ago):
    # Given commitquality.com/add-product

    # Given the date field has a date up to 100 years before the current date
    date = AddProductPage.get_date_num_years_ago(int(years_ago))
    add_product_page.type_field(date[1] + date[2] + date[0], AddProductPage.DATE_FIELD)

    # When you tab away from the date field
    add_product_page.tab_to_next_element()

    # Then no errors appear on the page
    assert (add_product_page.errors_exist() == False)


def test_tab_away_date_tomorrow(add_product_page):
    # Given commitquality.com/add-product

    # Given the date field has the date from tomorrow input
    date = AddProductPage.get_date_tomorrow()
    add_product_page.type_field(date[1] + date[2] + date[0], AddProductPage.DATE_FIELD)

    # When you tab away from the date field
    add_product_page.tab_to_next_element()

    # Then this error will appear above the date field: "Date must not be in the future."
    text = add_product_page.get_div_after_element(AddProductPage.DATE_LABEL).text
    assert text == "Date must not be in the future."

    # And this error will appear above the submit/cancel buttons: "Errors must be resolved before submitting"
    text = add_product_page.get_all_fields_validation_text()
    assert text == "Errors must be resolved before submitting"


def test_tab_away_date_leap_day_invalid(add_product_page):
    # Given commitquality.com/add-product

    # Given the date field has a leap day from a non-leap year input
    add_product_page.type_field("02292015", AddProductPage.DATE_FIELD)

    # When you tab away from the date field
    add_product_page.tab_to_next_element()

    # Then this error will appear above the date field: "Invalid date."
    # Note: I made up this error text myself, since I knew the existing error text was inaccurate.
    #       If this were a real product, I'd consult the design for the correct error text
    text = add_product_page.get_div_after_element(AddProductPage.DATE_LABEL).text
    assert text == "Invalid date."

    # And this error will appear above the submit/cancel buttons: "Errors must be resolved before submitting"
    text = add_product_page.get_all_fields_validation_text()
    assert text == "Errors must be resolved before submitting"


def test_tab_away_date_leap_day_valid(add_product_page):
    # Given commitquality.com/add-product

    # Given the date field has a leap day from a leap year input
    add_product_page.type_field("02292016", AddProductPage.DATE_FIELD)

    # When you tab away from the date field
    add_product_page.tab_to_next_element()

    # Then no errors appear on the page
    assert (add_product_page.errors_exist() == False)


def test_tab_order(add_product_page):
    # Given commitquality.com/add-product

    # When you tab through all elements on the pages
    # Then the elements will be focused upon in the correct order
    tab_order = [AddProductPage.PRODUCTS_LINK,
                 AddProductPage.ADD_PRODUCT_LINK,
                 AddProductPage.PRACTICE_LINK,
                 AddProductPage.LEARN_LINK,
                 AddProductPage.LOGIN_LINK,
                 AddProductPage.NAME_FIELD,
                 AddProductPage.PRICE_FIELD,
                 AddProductPage.DATE_FIELD,
                 AddProductPage.DATE_FIELD,
                 AddProductPage.DATE_FIELD,
                 AddProductPage.SUBMIT_BUTTON,
                 AddProductPage.CANCEL_BUTTON
                 ]
    
    for i in range(len(tab_order)):
        add_product_page.tab_to_next_element()
        focused_element = add_product_page.get_focused_element()
        assert focused_element == add_product_page.get_element(tab_order[i])