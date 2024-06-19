from Tests.Combined.LastMile.steps_android import base_steps as android_base
from Tests.Combined.LastMile.steps_ios import base_steps as ios_base


def before_all(context):
    context.android_base_fixture = android_base.BaseFixture()
    context.ios_base_fixture = ios_base.BaseFixture()


def before_scenario(context, scenario):
    if 'android' in scenario.tags:
        driver = context.android_base_fixture.setUp(context)
        print('Successfully setup Android device')
    elif 'ios' in scenario.tags:
        driver = context.ios_base_fixture.setUp(context)
        print("Successfully setup IOS device")





