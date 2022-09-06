from behave import *
from pages.page import Page


@step('I am directed to the "{route}" page')
def check_url(context, route):
    url = f"{context.base_url}{route}"
    page = Page(context.driver)
    nav = page.does_url_equal(url)
    assert nav, f"expected url to be {url} but it was not"


@step("an alert does not appear")
def check_alert_does_not_appear(context):
    page = Page(context.driver)
    alert = page.check_for_alert()
    assert alert is False, "Expected no alert to be seen, but one is present on the page"
