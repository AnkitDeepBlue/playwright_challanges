import pytest
import allure


@pytest.mark.table_test
@allure.feature('Table Sorting')
@allure.description("This is to sort table by columns and assert the sorting")
@pytest.mark.parametrize("column_name, order", [("Name", "sorting_desc"), ("Age", "sorting_desc")])
def test_sorting_table_by_column(table_page, column_name, order):
    with allure.step(f"Loading the table page"):
        table_page.load()

    with allure.step(f"Sorting the table by column: {column_name} with order: {order}"):
        final_sorting_details = table_page.sort_by_column(column_name, order)

    with allure.step("Asserting that the table is sorted correctly"):
        assert {column_name: order} == final_sorting_details, \
            f"Expected sorting: {{'{column_name}': '{order}'}}, but got: {final_sorting_details}"

    with allure.step("Attaching screenshot of the sorted table"):
        table_page.bot.take_screenshot(name=f"sorted_by_{column_name}")


@pytest.mark.table_test
@allure.feature('Table Search')
@allure.description("This is to search the names in table and validate it appears in row")
@pytest.mark.parametrize("name", ["S. Frost", "H. Martin"])
def test_table_search(table_page, name):
    with allure.step(f"Loading the table page"):
        table_page.load()

    with allure.step(f"Searching for the name: {name}"):
        table_page.search(name)

    with allure.step(f"Asserting that the search results contain the text: {name}"):
        found_text = table_page.search_contains_text(name)
        assert found_text, f"Text '{name}' is not found in search results."

    with allure.step("Attaching screenshot of the search results"):
        table_page.bot.take_screenshot(name=f"search_result_for_{name}")