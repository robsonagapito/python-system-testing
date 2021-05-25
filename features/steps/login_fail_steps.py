from behave import given, when, then, step
from hamcrest import assert_that, equal_to

@then(u'user should see fail page with "{result}" message')
def user_should_see_fail_page_with_message(context, result):
	assert_that(result, equal_to(context.loginFail.get_result()))