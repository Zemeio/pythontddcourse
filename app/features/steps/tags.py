from behave import (
    use_step_matcher,
    when,
    then,
    given,
    step,
)

from core import models
from core.models import Tag

use_step_matcher("cfparse")


def create_tag(context, tagname="Vegan", user=None):
    if not user:
        user = context.user
    tag = models.Tag.objects.create(
        user=user,
        name=tagname
    )
    context.tag = tag
    return tag


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


@given('Recipe "{recipename}" has a tag named "{tagname}"')
def step_impl(context, recipename, tagname):
    """
    :type context: behave.runner.Context
    """
    recipe = next(i for i in context.recipes if i.title == recipename)
    tag = create_tag(context, tagname=tagname)
    recipe.tags.add(tag)


@step('I have a tag "{tagname}" for the user "{email}"')
def step_impl(context, tagname, email):
    """
    :type context: behave.runner.Context
    """
    user = context.users[email]
    create_tag(context, tagname, user)


@step('Tag with name "{tagname}" exists in the database for my user')
def step_impl(context, tagname):
    """
    :type context: behave.runner.Context
    """
    exists = Tag.objects.filter(
        user=context.user,
        name=tagname,
    ).exists()

    context.test_case.assertTrue(exists)
