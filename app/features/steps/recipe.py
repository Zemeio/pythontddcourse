from behave import (
    use_step_matcher,
    when,
    then,
    given,
    step,
)

from core import models

use_step_matcher("cfparse")


def create_tag(context, tagname="Vegan", user=None):
    if not user:
        user = context.user
    tag = models.Tag.objects.create(
        user=user,
        name=tagname
    )
    context.tag = tag


@when('I create a tag named "{tagname}"')
def step_impl(context, tagname):
    """
    :type context: behave.runner.Context
    """
    create_tag(context, tagname)


@then('My tags string representation is "{tagname}"')
def step_impl(context, tagname):
    """
    :type context: behave.runner.Context
    """
    context.test_case.assertEqual(str(context.tag), tagname)


@given('I have a tag named "{tagname}"')
def step_impl(context, tagname):
    """
    :type context: behave.runner.Context
    """
    create_tag(context, tagname=tagname)


@step('I have a tag "{tagname}" for the user "{email}"')
def step_impl(context, tagname, email):
    """
    :type context: behave.runner.Context
    """
    user = context.users[email]
    create_tag(context, tagname, user)
