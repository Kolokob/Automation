from Steps.steps_web import base_steps as web_base
from Steps.steps.web_steps import *
base = BaseFixture()

def before_all(context):
    context.web_base_fixture = web_base.BaseFixture()


def before_scenario(context, scenario):
    driver = context.web_base_fixture.setUp(context, scenario.tags[1])







