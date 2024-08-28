import pytest
import allure


@allure.feature('Table Sorting')
@allure.description("This is to sort table by columns and assert the sorting")
@pytest.mark.parametrize("column_name, order", [("Name", "sorting_desc"), ("Age", "sorting_desc")])
def test_sorting_table_by_column(table_page, column_name, order):
    table_page.load()
    final_sorting_details = table_page.sort_by_column(column_name, order)
    assert {column_name:order} == final_sorting_details


@allure.feature('Table Search')
@allure.description("This is to search the names in table and validate it appears in row")
@pytest.mark.parametrize("name", ["S. Frost", "H. Martin"])
def test_table_search(table_page, name):
    table_page.load()
    table_page.search(name)
    found_text = table_page.search_contains_text(name)
    assert found_text, f"Text '{name}' not found in search results."
