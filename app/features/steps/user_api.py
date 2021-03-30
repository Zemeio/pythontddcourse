from behave import (
    use_step_matcher,
    when,
    then,
    step,
)

from django.urls import reverse
from rest_framework import status

CREATE_USER_URL = reverse("user:create")


use_step_matcher("cfparse")


@when("I call the Create User API with the following payload:")
@when("I call the Create User API with the following payload")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    email, user, password = context.table.rows[0]
    payload = {
        "email": email,
        "name": user,
        "password": password
    }

    context.url_response = context.test_client.post(CREATE_USER_URL, payload)


@then("I get a 201 CREATED response")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_case.assertEqual(context.url_response.status_code, status.HTTP_201_CREATED,
                                  "Expected 201 CREATED, but got %d" % context.url_response.status_code)


@step('Password is not returned in the API response')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_case.assertNotIn("password", context.url_response.data)


@then("I get a 400 BAD REQUEST response")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_case.assertEqual(context.url_response.status_code, status.HTTP_400_BAD_REQUEST,
                                  "Expected 400 BAD REQUEST, but got %d" % context.url_response.status_code)
