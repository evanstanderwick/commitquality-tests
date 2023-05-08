"""
Multi-page workflow tests for commitquality.com
"""

# 
# imports
# 

from pages.add_product import AddProductPage
from pages.products import ProductsPage
import pytest


# 
# tests
# 

@pytest.mark.parametrize("num_iterations", [1,2])
def test_add_product_filter_n_times(products_page, add_product_page, num_iterations):
    products_added = 0
    for i in range(num_iterations):
        # Given commitquality.com/add-product
    
        # Given you've just added another product whose name starts with "test "
        add_product_page.type_field("test " + str(i), AddProductPage.NAME_FIELD)
        add_product_page.type_field("01012020", AddProductPage.DATE_FIELD)
        add_product_page.type_field("5", AddProductPage.PRICE_FIELD)
        add_product_page.click(AddProductPage.SUBMIT_BUTTON)
        products_added += 1

        # Given you've filled out the filter field with "test "
        add_product_page.type_field("test", ProductsPage.FILTER_FIELD)

        # When you click the filter button
        add_product_page.click(ProductsPage.FILTER_BUTTON)

        # Then the product you've just added is found
        # And the other products you've added named with the same prefix "test " are found

        num_rows = len(products_page.get_products_table_rows()) - 1 # -1 to account for header row
        assert num_rows == products_added

        first_row_id = int(products_page.get_products_table_first_product_data()[0].text)
        for id in range(first_row_id, first_row_id - num_rows, -1):
            row = products_page.get_products_table_row_data(id)
            name = row[1].text
            price = row[2].text
            date = row[3].text

            assert name[:5] == "test "
            assert price == "5"
            assert date == "2020-01-01"

        products_page.click(ProductsPage.ADD_PRODUCT_BUTTON)


def test_add_product_refresh(products_page, add_product_page):
    # Given commitquality.com/add-product

    # Given you've just added a new product
    add_product_page.type_field("test", AddProductPage.NAME_FIELD)
    add_product_page.type_field("01012020", AddProductPage.DATE_FIELD)
    add_product_page.type_field("5", AddProductPage.PRICE_FIELD)
    add_product_page.click(AddProductPage.SUBMIT_BUTTON)

    # When you refresh the page
    products_page.refresh()

    # The product you added will no longer be there
    products_names = products_page.get_products_names()
    assert "test" not in products_names


def test_add_product_cancel(products_page, add_product_page):
    # Given commitquality.com/add-product

    # Given you've just added a new product
    add_product_page.type_field("test", AddProductPage.NAME_FIELD)
    add_product_page.type_field("01012020", AddProductPage.DATE_FIELD)
    add_product_page.type_field("5", AddProductPage.PRICE_FIELD)
    add_product_page.click(AddProductPage.SUBMIT_BUTTON)

    # When you cancel adding another product
    products_page.click(ProductsPage.ADD_PRODUCT_BUTTON)
    add_product_page.click(AddProductPage.CANCEL_BUTTON)

    # The product you added will still be at the top of the products list
    row = products_page.get_products_table_first_product_data()
    assert row[1].text == "test"
    assert row[2].text == "5"
    assert row[3].text == "2020-01-01"