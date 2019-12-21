from locust import HttpLocust, TaskSet, between, task


class UserBehavior(TaskSet):

    @task(1)
    def get_calls(self):
        self.client.get('/words')

    @task(1)
    def get_word(self):
        self.client.get('/word/1')

    @task(2)
    def create_word(self):
        payload = {
            "word": "hello",
            "translation": "привіт",
        }
        self.client.post('/words', json=payload)

    @task(2)
    def update_task(self):
        payload = {
            "word": "hello",
            "translation": "привіт",
            "done": "True",
        }
        self.client.put('/words/1', json=payload)

    @task(2)
    def delete_word(self):
        self.client.delete('/words/2')


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1.0, 2.0)