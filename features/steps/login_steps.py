from behave import given, when, then


@given('Open Reelly login page')
def open_login_page(context):
    context.app.login_page.open_login_page()


@when('User logs in to the site')
def login_to_site(context):
    context.app.login_page.login_to_site()