from behave import (
    use_step_matcher,
    step,
    when,
    then,
)

from core import models

use_step_matcher("cfparse")


@step('I have an ingredient associated with my user named "{ingredient_name}"')
def step_impl(context, ingredient_name):
    """
    :type ingredient_name: str
    :type context: behave.runner.Context
    """
    create_ingredient(context, ingredient_name)


def create_ingredient(context, ingredient_name="Salt"):
    context.ingredient = models.Ingredient.objects.create(
        user=context.user,
        name=ingredient_name,
    )
    return context.ingredient


@step('Recipe "{recipename}" has an ingredient named "{ingredient_name}"')
def step_impl(context, recipename, ingredient_name):
    """
    :type context: behave.runner.Context
    """
    recipe = next(i for i in context.recipes if i.title == recipename)
    recipe.tags.add(create_ingredient(context, ingredient_name=ingredient_name))


@when("I take the string representation of my ingredient")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.string_representation = str(context.ingredient)


@then('The string representation is "{ingredient_name}"')
def step_impl(context, ingredient_name):
    """
    :type ingredient_name: str
    :type context: behave.runner.Context
    """
    context.test_case.assertEquals(context.string_representation, ingredient_name)


@step('I have an ingredient "{ingredient_name}" for the user "{email}"')
def step_impl(context, ingredient_name, email):
    """
    :type email: str
    :type ingredient_name: str
    :type context: behave.runner.Context
    """
    user = context.users[email]
    models.Ingredient.objects.create(
        user=user,
        name=ingredient_name,
    )
