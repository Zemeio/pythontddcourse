from behave import (
    use_step_matcher,
    when,
    step,
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
