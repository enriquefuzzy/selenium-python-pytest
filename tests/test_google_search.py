import pytest
import os
ROOT_DIR = os.path.abspath(os.curdir)
from selenium import webdriver
from pytest_bdd import given, when, then, scenarios
from pytest_bdd.parsers import parse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# Define the feature file(s) to be used
scenarios(f'{ROOT_DIR}/features')

@pytest.fixture(scope="module")
def driver():
    # Create an instance of the Chrome WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Close the browser
    driver.quit()

@given("the user is on Google")
def given_user_on_google(driver):
    # Navigate to Google
    driver.get("https://www.google.com")

@when(parse("the user searches for {search_term}"))
@when("the user searches for {search_term}")
def when_user_searches(driver, search_term):
    # Locate the search input field and enter the search term
    search_input = driver.find_element(By.CSS_SELECTOR, "[name=q]")
    search_input.send_keys(search_term)
    search_input.submit()

@then("Dog results are displayed")
def then_dog_results_displayed(driver):
    # Verify that the search results contain the word "Dog"
    search_results = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH,"//div[@data-attrid='title'][contains(text(), 'Dog')]"))
    search_results = driver.find_element(By.XPATH,"//div[@data-attrid='title'][contains(text(), 'Dog')]")
    assert search_results, "Dog results are not displayed"
