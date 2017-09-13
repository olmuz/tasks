from behave import given, when, then
from pages.calculate_page import CalculatePage


@given("form that uses method from task1")
def step(context): 
	CalculatePage(context.browser).open()



@when("Fill text form") 
def step(context): 
	for row in context.table: 
		CalculatePage(context.browser).find_element(row['name']).send_keys(row['value'])
 
 
@when("user press '{name}' button") 
def step(context, name): 
	CalculatePage(context.browser).find_element(name).click()


@then('new form appeared below with return values')
def step(context):
	assert CalculatePage(context.browser).is_visible