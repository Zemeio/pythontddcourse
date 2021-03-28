from behave import (
    when,
    then,
    step,
    given,
    use_step_matcher,
)
from django.contrib.auth import get_user_model

use_step_matcher("cfparse")


GENERIC_EMAIL = "email@domain.co.jp"
GENERIC_PASSWORD = "pass123"


@when("a user has been created with the following details:")
@when("a user has been created with the following details")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    email, user, password = context.table.rows[0]
    user = get_user_model().objects.create_user(
        email=email,
        password=password,
    )
    context.user = user


@then('A user "user" is created with the following info:')
@then('A user "user" is created with the following info')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    assert hasattr(context, "user"),\
        "User not created or not loaded into the context"

    email, username, password = context.table.rows[0]
    user = context.user
    assert user.email == email
    assert user.check_password(password)


@given('I have the email "{email}"')
def step_impl(context, email):
    """
    :type context: behave.runner.Context
    """
    context.email = email


@when("I create a user with my email")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user = get_user_model().objects.create_user(
        email=context.email,
        password=GENERIC_PASSWORD,
    )


@then("The user is registered with the email in lower case")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    expected = context.email.lower()
    assert context.user.email == expected,\
        "User email did not match expected %s" % expected


@when("I create a user without providing an email")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        context.user = get_user_model().objects.create_user(
            email=None,
            password=GENERIC_PASSWORD
        )
    except Exception as e:
        context.exception = e


@then("An error is raised")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert hasattr(context, "exception"), "Error is not being raised"


@step("The error is a ValueError")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert isinstance(context.exception, ValueError),\
        "error is of type %s" % type(context.exception)


@when("I create a super user using django support")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user = get_user_model().objects.create_superuser(
        email=GENERIC_EMAIL,
        password=GENERIC_PASSWORD,
    )


@then("User is a superuser")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.user.is_superuser, "User is not a superuser"


@step("User is a staff")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.user.is_staff, "User is not a staff"
