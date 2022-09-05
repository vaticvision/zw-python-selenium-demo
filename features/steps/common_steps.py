from behave import *
from pages.common import CommonPage


@step('I am directed to the "{route}" page')
def check_url(context, route):
    url = f"{context.base_url}{route}"
    common = CommonPage(context.driver)
    nav = common.does_url_equal(url)
    assert nav, f"expected url to be {url} but it was not"


@step("an alert does not appear")
def check_alert_does_not_appear(context):
    common = CommonPage(context.driver)
    alert = common.check_for_alert()
    assert alert is False, "Expected no alert to be seen, but one is present on the page"
