from behave import (
    use_step_matcher,
    given,
    step,
    then,
)
from django.contrib.auth import get_user_model
from django.test import Client
from rest_framework.test import APIClient

use_step_matcher("re")


@given("I have a test client")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_client = Client()


@step("I have a user logged in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.admin_user = get_user_model().objects.create_superuser(
        email="admin@myapp.co.jp",
        password="password123",
    )

    context.test_client.force_login(context.admin_user)


@step("I have a regular user unauthenticated")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.regular_user = get_user_model().objects.create_user(
        email="test@myapp.co.jp",
        password="password123",
        name="Test user full name"
    )


@then("My regular user appears in the response")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_case.assertContains(context.url_response, context.regular_user)


@given("I have an API test client")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_client = APIClient()
