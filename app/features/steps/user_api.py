from behave import (
    use_step_matcher,
    when,
    then,
    step,
)

from django.urls import reverse
from rest_framework import status

CREATE_USER_URL = reverse("user:create")
ME_USER_URL = reverse("user:me")


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


@when("I call the ME API")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.url_response = context.test_client.get(ME_USER_URL)


@then("I get a 401 UNAUTHORIZED response")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_case.assertEqual(context.url_response.status_code, status.HTTP_401_UNAUTHORIZED,
                                  "Expected 401 UNAUTHORIZED, but got %d" % context.url_response.status_code)


@step('My test client is authenticated for user "{email}"')
def step_impl(context, email):
    """
    :type context: behave.runner.Context
    """
    user = context.users[email]
    context.test_client.force_authenticate(user=user)


@step('The response contains the email "{email}"')
def step_impl(context, email):
    """
    :type context: behave.runner.Context
    """

    context.test_case.assertIn("email", context.url_response.data)
    context.test_case.assertEqual(email, context.url_response.data["email"])


@step('The response contains the name "{user}"')
def step_impl(context, user):
    """
    :type context: behave.runner.Context
    """
    context.test_case.assertIn("name", context.url_response.data)
    context.test_case.assertEqual(user, context.url_response.data["name"])


@when("I call the ME API with the post method")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.url_response = context.test_client.post(ME_USER_URL, {})


@when("I call the ME API with the following payload:")
@when("I call the ME API with the following payload")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    name, password = context.table.rows[0]
    payload = {
        "name": name,
        "password": password
    }
    context.url_response = context.test_client.patch(ME_USER_URL, payload)


@step('The DB is refreshed for the user "{email}"')
def step_impl(context, email):
    """
    :type context: behave.runner.Context
    """
    user = context.users[email]
    user.refresh_from_db()
