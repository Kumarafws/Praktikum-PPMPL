from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    host = "http://127.0.0.1:5000"
    wait_time = between(1, 3)

    @task(1)
    def get_all_users(self):
        self.client.get("/users")

    @task(2)
    def get_single_user(self):
        self.client.get("/users/1")

    @task(3)
    def create_user(self):
        self.client.post("/users", json={
            "name": "New User",
            "email": "newuser@example.com"
        })

    @task(4)
    def update_user(self):
        self.client.put("/users/1", json={
            "name": "Updated User",
            "email": "updateduser@example.com"
        })

    @task(5)
    def delete_user(self):
        self.client.delete("/users/3")