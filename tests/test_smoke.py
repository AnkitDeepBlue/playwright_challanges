import pytest
import allure


@pytest.mark.smoke
@allure.feature('This is smoke test')
@allure.story('Testing smoke story')
@allure.description("SMOKE TEST")
def smoke_test():
   pass