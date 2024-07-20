from Steps.steps_ios import base_steps as ios_base
from Steps.steps.ios_steps import *
base = BaseFixture()


driver_v = 'com.senpex.customer'
client_v = 'com.softmindup.senpex'

def before_all(context):
    context.ios_base_fixture = ios_base.BaseFixture()

def before_scenario(context, scenario):
    context.mobile_platform = 'ios'
    bundle_id = driver_v if 'driver' in scenario.tags else client_v
    print(f"Setting up iOS with bundle_id: {bundle_id}")  # Отладочное сообщение
    context.ios_base_fixture.setUp(context, bundle_id)








