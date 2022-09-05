from behave import *
from pages.login import LoginPage


@step("I enter my username")
def enter_test_user_username(context):
    login = LoginPage(context.driver)
    login.enter_username(context.username)


@when('I enter the username "{username}"')
def enter_password_manual(context, username):
    login = LoginPage(context.driver)
    login.enter_username(username)


@step("I enter my password")
def enter_test_user_password(context):
    login = LoginPage(context.driver)
    login.enter_password(context.password)


@step('I enter the password "{password}"')
def enter_password_manual(context, password):
    login = LoginPage(context.driver)
    login.enter_password(password)


@step("I click the Log In button")
def click_log_in_button(context):
    login = LoginPage(context.driver)
    login.click_log_in()


@when("I click the help link")
def click_help_link(context):
    login = LoginPage(context.driver)
    login.click_help_link()


@when("I click the help link in the error message")
def click_help_in_error(context):
    login = LoginPage(context.driver)
    login.click_help_link_error()


@then("I am taken to the forgot password form")
def check_for_forgot_password(context):
    login = LoginPage(context.driver)
    password_reset_appears = login.password_reset_button_appears()
    assert password_reset_appears, "Expected to be on the password reset form, but we are not"


@then('an error appears that includes text "{expected_text}"')
def check_error_text(context, expected_text):
    login = LoginPage(context.driver)
    error_text = login.get_error_text()
    assert expected_text in error_text,\
        f"Error did not display correct text. Expected {expected_text}, got {error_text}"
