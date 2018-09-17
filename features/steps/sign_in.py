from behave import given, then, when
from time import sleep


@given('I navigate to the "{url}"')
def go_website(context, url):
    context.home_page.navigate(url)


@when('Verify to the "{title}"')
def verify_title(context, title):
    subtitle = context.home_page.get_page_title()
    assert subtitle == title


@when('Click to the "{aux}"')
def sign_in(context, aux):
    context.home_page.click_anythings(aux)


@then('Click to the "{aux}"')
def sign_in(context, aux):
    context.home_page.click_anythings(aux)


@given('Click to the "{aux}"')
def sign_in(context, aux):
    context.home_page.click_anythings(aux)


@when('Click to "{day}" "{month}" "{year}"')
def data(context, day, month, year):
    context.home_page.insert_data(day, month, year)


@then('Check "{subject}"')
def check(context, subject):
    aux = context.home_page.get_check()
    assert subject == aux, "### Error!!! Resultados diferentes ###"


@when('Insert to "{email}" "{password}"')
def login(context, email, password):
    context.home_page.login(email, password)


@when('We must be to buy item(s)')
def number_items(context):
    sleep(5)
    context.home_page.number_items()


@then('Checkend "{end}"')
def check_end(context, end):
    sleep(5)
    aux = context.home_page.check_end()
    assert end == aux, "### Error!!! Resultados diferentes ###"

@when('Putting to "{end}" "{info}"')
def step_impl(context,end, info):
    context.home_page.insert_anythings(end, info)

