from behave import when


@when('Settings option is clicked')
def click_settings_option(context):
    context.app.nav_menu.click_settings_option()