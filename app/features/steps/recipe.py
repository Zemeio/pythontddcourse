from behave import (
    use_step_matcher,
    when,
    then,
    given,
    step,
)

from core import models

use_step_matcher("cfparse")


@given("I have recipes for my user with the following info:")
@given("I have recipes for my user with the following info")
@when("I create recipes for my user with the following info:")
@when("I create recipes for my user with the following info")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    user = context.user
    data_table = context.table.rows
    create_recipes_for_user(context, data_table, user)


def create_recipes_for_user(context, data_table, user):
    if not hasattr(context, "recipes"):
        context.recipes = []
    for title, time, price in data_table:
        recipe = models.Recipe.objects.create(
            user=user,
            title=title if title else "Sample Recipe",
            time_minutes=int(time) if time else 10,
            price=float(price) if price else 5.00,
        )
        context.recipes.append(recipe)


@then('The string representation of my recipe is "{recipe_name}"')
def step_impl(context, recipe_name):
    """
    :type recipe_name: str
    :type context: behave.runner.Context
    """
    recipe = context.recipes[0]
    context.test_case.assertEquals(str(recipe), recipe_name)


@step('I have recipes for the user "{email}" with the following info:')
@step('I have recipes for the user "{email}" with the following info')
def step_impl(context, email):
    """
    :type context: behave.runner.Context
    """
    user = context.users[email]
    data_table = context.table.rows
    create_recipes_for_user(context, data_table, user)
