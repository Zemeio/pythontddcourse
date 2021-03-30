from behave import (
    use_step_matcher,
    when,
    step,
)
from django.urls import reverse


use_step_matcher("cfparse")


TOKEN_URL = reverse("user:token")


@step("The response should contain the token keyword")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_case.assertIn("token", context.url_response.data)


@step("The response should NOT contain the token keyword")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_case.assertNotIn("token", context.url_response.data)


@when('I call the Create Token API for my user "{email}" with password "{password}"')
def step_impl(context, email, password):
    """
    :param password: str
    :param email: str
    :type context: behave.runner.Context
    """
    payload = {
        "email": email,
        "password": password,
    }
    context.url_response = context.test_client.post(TOKEN_URL, payload)


@when("I call the Create Token API without a user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    payload = {
        "email": "email@test.co.jp",
        "password": "",
    }
    context.url_response = context.test_client.post(TOKEN_URL, payload)


@when("I call the Create Token API without a password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    payload = {
        "email": "",
        "password": "password",
    }
    context.url_response = context.test_client.post(TOKEN_URL, payload)
