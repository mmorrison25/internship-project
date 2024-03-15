from behave import when


@when('Contact us option is clicked')
def click_contact_us_button(context):
    context.app.settings_page.click_contact_us_button()