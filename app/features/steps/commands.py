from behave import (
    use_step_matcher,
    given,
    when,
    then,
)

from django.core.management import call_command
from django.db import OperationalError

from features.steps.mocker import patch_

use_step_matcher("cfparse")


@when('I call the command "{command}"')
def step_impl(context, command):
    """
    :param command: str
    :type context: behave.runner.Context
    """
    pass
    call_command(command_name=command)


@then('The DB is called exactly "{number}" times')
def step_impl(context, number):
    """
    :param number: int
    :type context: behave.runner.Context
    """
    context.test_case.assertEqual(
        context.dbmock.call_count, int(number),
        "Db was called %s times" % context.dbmock.call_count)


@given('The DB works on the "{number}" try')
def step_impl(context, number):
    """
    :type context: behave.runner.Context
    """

    context.dbmock = patch_(context, "django.db.utils.ConnectionHandler.__getitem__")
    number = int(number)
    if number > 1:
        context.dbmock.side_effect = [OperationalError] * (number - 1) + [True]
    else:
        context.dbmock.return_value = True


@given("The function sleep is mocked")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.sleepmock = patch_(context, "time.sleep")
    context.sleepmock.return_value = True
