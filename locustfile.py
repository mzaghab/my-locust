from locust import task, FastHttpUser

class MyUser(FastHttpUser):
    @task
    def t(self):
        extra_headers = {"my_header": "my_value"}
        with self.rest("POST", "/", json={"foo": 1}) as resp:
            if resp.js is None:
                pass # no need to do anything, already marked as failed
            elif "bar" not in resp.js:
                resp.failure(f"'bar' missing from response {resp.text}")
            elif resp.js["bar"] != 42:
                resp.failure(f"'bar' had an unexpected value: {resp.js['bar']}")
