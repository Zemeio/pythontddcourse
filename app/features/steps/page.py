from behave import *
from django.urls import reverse

use_step_matcher("cfparse")


pages = {
    "admin core user changelist": "admin:core_user_changelist"
}


@when('I access the "{page_name}" page')
def step_impl(context, page_name):
    """
    :param page_name: str
    :type context: behave.runner.Context
    """

    base_url = pages[page_name]
    context.absolute_url = reverse(base_url)
    context.url_response = context.test_client.get(context.absolute_url)


@when("I access the edit user page for my regular user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.absolute_url = reverse("admin:core_user_change", args=[context.regular_user.id])
    context.url_response = context.test_client.get(context.absolute_url)


@then("I get a 200 OK response")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.url_response.status_code == 200


@when("I access the create user page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.absolute_url = reverse("admin:core_user_add")
    context.url_response = context.test_client.get(context.absolute_url)