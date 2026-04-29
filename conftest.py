import pytest
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome=yield
    result=outcome.get_result()
    setattr(item,result.when,result)
    #result.when--> 3 status setup call teardown