import os
from selenium import webdriver


def before_all(context):
    # things that happen before the tests run

    # grab some environment variables we'll need for our tests
    context.username = os.getenv("DEMO_TESTS_USERNAME")
    context.password = os.getenv("DEMO_TESTS_PASSWORD")
    context.base_url = os.getenv("DEMO_BASE_URL")


def before_scenario(context, scenario):
    # things that happen before each test

    # start a new chrome instance
    context.driver = webdriver.Chrome()

    # nav to Hudl login page
    context.driver.get(f"{context.base_url}/login")


def after_scenario(context, scenario):
    # things that happen after each scenario

    # take a screenshot if our test fails
    if scenario.status == "failed":
        # behavex automatically sets context.evidence_path. If we're not using behavex this can cause an error
        if hasattr(context, "evidence_path"):
            screenshot_path = f"{context.evidence_path}/{scenario.name}.png"
        else:
            # check for a screenshots folder and create one if none exist
            if not os.path.exists('screenshots'):
                os.makedirs('screenshots')
            screenshot_path = f"screenshots/{scenario.name}.png"
        context.driver.save_screenshot(screenshot_path)
    # quit the driver
    context.driver.quit()
