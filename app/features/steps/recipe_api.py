from behave import (
    use_step_matcher,
    when,
    step,
)
from rest_framework.reverse import reverse

from core.models import Tag
from recipe.serializers import TagSerializer

use_step_matcher("cfparse")


TAGS_URL = reverse("recipe:tag-list")


@when("I call the tag list API")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.url_response = context.test_client.get(TAGS_URL)
    pass


@step("All of my tags are in the response ordered by name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    tags = Tag.objects.all().order_by("-name")
    serializer = TagSerializer(tags, many=True)
    context.test_case.assertEquals(context.url_response.data, serializer.data)


@step('The response contains "1" key')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    data = context.url_response.data
    context.test_case.assertEquals(len(data), 1)


@step('the tag "{tagname}" is returned in the response')
def step_impl(context, tagname):
    """
    :type context: behave.runner.Context
    """
    data = context.url_response.data
    context.test_case.assertEquals(data[0]["name"], tagname)
