from Steps.steps_android import base_steps as android_base
from Steps.steps_ios import base_steps as ios_base

driver_v = 'com.senpex.customer'
client_v = 'com.softmindup.senpex'


def before_all(context):
    context.android_base_fixture = android_base.BaseFixture()
    context.ios_base_fixture = ios_base.BaseFixture()


def before_scenario(context, scenario):
    print(scenario.tags)
    if 'android' in scenario.tags:
        bundle_id = driver_v if 'driver' in scenario.tags else client_v
        driver = context.android_base_fixture.setUp(context, bundle_id)
    elif 'ios' in scenario.tags:
        bundle_id = driver_v if 'driver' in scenario.tags else client_v
        driver = context.ios_base_fixture.setUp(context, bundle_id)





