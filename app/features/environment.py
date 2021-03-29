from django.test import TestCase


def before_all(context):
    context.test_case = TestCase()
