from django.test import TestCase


def before_all(context):
    context.test_case = TestCase()


def before_scenario(context, scenario):
    context.patches = []


def after_scenario(context, scenario):
    for mock in context.patches:
        mock.stop()
