from locust import HttpUser, task, between, events
from locust.env import Environment
from locust.stats import stats_printer
import gevent

# Define your user behavior
class WebsiteUser(HttpUser):
    host = "http://127.0.0.1:8001"
    wait_time = between(1, 2)  # Wait time between tasks

    @task
    def my_task(self):
        self.client.get("/")  # Replace with your actual request

# Setup Environment and Runner
env = Environment(user_classes=[WebsiteUser])
env.create_local_runner()

env.create_web_ui("127.0.0.1", 8089)

# Event handler to stop the test after reaching 10,000 requests
def stop_test(request_type, name, response_time, response_length, exception, context, start_time, url, **kwargs):
    total_requests = sum([stats.num_requests for stats in env.runner.stats.entries.values()])
    print("Total requests: ", total_requests)
    if total_requests >= 10000:  # Stop the test when 10,000 requests are reached
        env.runner.quit()

# Register event listeners
def setup_listeners():
    events.request.add_listener(stop_test)

setup_listeners()

# Start the test with 20 users at a spawn rate of 20 users per second
env.runner.start(user_count=20, spawn_rate=20)

# In case you want to print stats in the console
gevent.spawn(stats_printer(env.stats))

# Wait for the runner greenlet to complete
env.runner.greenlet.join()
