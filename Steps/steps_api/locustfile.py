# This file is designed in order to perform stress testing
from locust import HttpUser, TaskSet, task, between
class UserBehavior(TaskSet):
    @task(1)
    def load_page(self):
        self.client.get("/")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)



# This is command to start it
# Write this is terminal and follow the instructions
# locust -f locustfile.py --host=https://v4-sandbox.senpex.com/