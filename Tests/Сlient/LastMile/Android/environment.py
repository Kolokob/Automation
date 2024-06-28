from Steps.steps_android import base_steps as android_base
from Steps.steps_ios import base_steps as ios_base
from Steps.steps_android.base_steps import BaseFixture
from Steps.steps_android import *
from Steps.steps_ios import *
from Steps.steps.ios_steps import *
from Steps.steps.android_steps import *
base = BaseFixture()

def before_all(context):
    context.android_base_fixture = android_base.BaseFixture()
    context.ios_base_fixture = ios_base.BaseFixture()


def before_scenario(context, scenario):
    if 'android' in scenario.tags:
        driver = context.android_base_fixture.setUp(context)
        print('Successfully setup Android device')
        # base.start_screen_recording(context, '/Users/kolokob/Desktop', f"{scenario.name.replace(' ', '_')}.mp4")
    elif 'ios' in scenario.tags:
        driver = context.ios_base_fixture.setUp(context)
        print("Successfully setup IOS device")

# def after_scenario(context, scenario):
#     base.stop_screen_recording(context, '/Users/kolokob/Desktop', filename=f"{scenario.name.replace(' ', '_')}.mp4")







