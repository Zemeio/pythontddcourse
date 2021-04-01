from behave import (
    use_step_matcher,
    when,
    then,
)

from core import models

use_step_matcher("cfparse")


@when("I create recipes for my user with the following info:")
@when("I create recipes for my user with the following info")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if not hasattr(context, "recipes"):
        context.recipes = []
    for title, time, price in context.table.rows:
        recipe = models.Recipe.objects.create(
            user=context.user,
            title=title,
            time_minutes=int(time),
            price=float(price),
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
