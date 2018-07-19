from behave import given, when, then, step
from hamcrest import assert_that, equal_to
from features.pages.login import Login
from features.pages.login_fail import LoginFail
from features.pages.login_ok import LoginOk

@given("user would like to log in application")
def user_would_like_to_log_in_application(context):
	context.login = Login(context.driverQA)
	context.loginOk = LoginOk(context.driverQA)
	context.loginFail = LoginFail(context.driverQA)
	context.login.open_url()

@given(u'user informs login with value equal "{user}" with id')
def user_informs_login_with_value_equal_with_id(context,user):
	context.login.fill_user(user)
	
@given(u'user informs password with value equal "{password}"')
def user_informs_password_with_value_equal(context,password):
	context.login.fill_password(password)

@when('user clicks on login button')
def user_clicks_on_login_button(context):
	context.login.click_ok()

@then(u'user should see page with "{result}" message')
def user_should_see_page_with_message(context, result):
	assert_that(result, equal_to(context.login.get_result()))