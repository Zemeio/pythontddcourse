from behave import (
    use_step_matcher,
    when,
    step,
    then,
)
from rest_framework.reverse import reverse

from core.models import Recipe
from recipe.serializers import RecipeSerializer, RecipeDetailSerializer

use_step_matcher("cfparse")


RECIPES_URL = reverse("recipe:recipe-list")


def detail_url(recipe_id):
    """Return the recipe detail url"""
    return reverse("recipe:recipe-detail", args=[recipe_id])


@when("I call the recipe list API")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.url_response = context.test_client.get(RECIPES_URL)


@step("All of the recipes are returned sorted by id")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    recipes = Recipe.objects.all().order_by("-id")
    serializer = RecipeSerializer(recipes, many=True)

    response_data = context.url_response.data

    context.test_case.assertEqual(serializer.data, response_data)


@step('The recipe for "{recipe_name}" should appear in the result')
def step_impl(context, recipe_name):
    """
    :type context: behave.runner.Context
    """
    data = context.url_response.data
    context.test_case.assertEquals(data[0]["title"], recipe_name)


@when('I call the recipe detail API for recipe "{recipe_name}"')
def step_impl(context, recipe_name):
    """
    :type context: behave.runner.Context
    """
    recipe = next(i for i in context.recipes if i.title == recipe_name)
    context.url_response = context.test_client.get(detail_url(recipe.id))


@then('The response should contain be equal to the "{recipe_name}" recipe in the database')
def step_impl(context, recipe_name):
    """
    :type context: behave.runner.Context
    """
    recipe = next(i for i in context.recipes if i.title == recipe_name)
    serializer = RecipeDetailSerializer(recipe)
    context.test_case.assertEquals(serializer.data, context.url_response.data)
