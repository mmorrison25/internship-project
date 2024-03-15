from behave import then
from selenium.webdriver.common.by import By

SOCIAL_MEDIA_ICON = (By.CSS_SELECTOR, '[class*="social-button"]')


@then('Verify {expected_amount} social media icons are displayed')
def verify_social_media_icons(context, expected_amount):
    expected_amount = int(expected_amount)
    social_media_icons = context.driver.find_elements(*SOCIAL_MEDIA_ICON)
    assert len(social_media_icons) == expected_amount, f'Expected {expected_amount} social icons but got {len(social_media_icons)}'
