from dataclasses import dataclass


@dataclass(frozen=True)
class LambdaTable:
    url: str = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
    name_column_header: str = "th:has-text('{column_name}')"
    table_rows: str = "table tbody tr"
    submit_button: str = "input[type='search']"
    row_locator: str = "table tbody tr:has-text('{text}')"
    search_input: str = "input[type = 'search']"
