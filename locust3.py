from locust import HttpUser, task, between, FastHttpUser
from locust.env import Environment
from locust.stats import stats_printer
import gevent
import time

# Define your user behavior
class WebsiteUser(FastHttpUser):
    wait_time = between(1, 2)  # Wait time between tasks

    @task
    def my_task(self):
        self.client.get("/")  # Your task here; replace with your actual path

# Environment setup and local runner
env = Environment(user_classes=[WebsiteUser], host="http://127.0.0.1:8001")
env.create_local_runner()

# Start the real-time status update system
def real_time_status_update():
    while True:
        # Displays the global task's internal performance situation
        total_requests = sum([stats.num_requests for stats in env.runner.stats.entries.values()])
        print(f"Total requests: {total_requests}")
        # Ends activity when a quantity of 1,000 is reached
        if total_requests >= 1000:
            print("Reached 1,000 requests. Halt...")
            env.runner.quit()
            break
        time.sleep(2)  # 10-second dialog frame halt

# Continues the function for displaying activity understanding in the working setting
gevent.spawn(real_time_status_update)

# Starting the application
env.create_web_ui("127.0.0.1", 8089)
env.runner.start(user_count=200, spawn_rate=1)
gevent.spawn(stats_printer(env.stats))
env.runner.greenlet.join()
env.web_ui.stop()
