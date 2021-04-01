from behave import (
    use_step_matcher,
    when,
    step,
    then,
)
from rest_framework.reverse import reverse

from core.models import Ingredient
from recipe.serializers import IngredientSerializer

use_step_matcher("cfparse")


INGREDIENTS_URL = reverse("recipe:ingredient-list")


@when("I call the ingredient list API")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.url_response = context.test_client.get(INGREDIENTS_URL)


@step("All of my ingredients are in the response ordered by name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    ingredients = Ingredient.objects.all().order_by("-name")
    serializer = IngredientSerializer(ingredients, many=True)
    context.test_case.assertEquals(context.url_response.data, serializer.data)


@step('the ingredient "{ingredient_name}" is returned in the response')
def step_impl(context, ingredient_name):
    """
    :type ingredient_name: str
    :type context: behave.runner.Context
    """
    data = context.url_response.data
    context.test_case.assertEquals(data[0]["name"], ingredient_name)


@when("I call the Ingredient API with the following payload:")
@when("I call the Ingredient API with the following payload")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    payload = {
        "name": context.table.rows[0][0],
    }
    context.url_response = context.test_client.post(INGREDIENTS_URL, payload)


@then('Ingredient with name "{ingredient_name}" exists in the database for my user')
def step_impl(context, ingredient_name):
    """
    :type ingredient_name: str
    :type context: behave.runner.Context
    """
    exists = Ingredient.objects.filter(
        user=context.user,
        name=ingredient_name,
    ).exists()
    context.test_case.assertTrue(exists)


@when("I call the Ingredient API with an empty name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    payload = {
        "name": "",
    }
    context.url_response = context.test_client.post(INGREDIENTS_URL, payload)
