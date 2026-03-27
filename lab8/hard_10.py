class DataLayer:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_all_users(self):
        return self.users

    def find_by_name(self, name):
        return [u for u in self.users if u["name"] == name]


class ServiceLayer:
    def __init__(self, data_layer):
        self.data = data_layer

    def register_user(self, name, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        user = {"name": name, "age": age}
        self.data.add_user(user)
        return user

    def get_adults(self):
        return [u for u in self.data.get_all_users() if u["age"] >= 18]

    def get_all_users(self):
        return self.data.get_all_users()


data = DataLayer()
service = ServiceLayer(data)

service.register_user("Иван", 25)
service.register_user("Мария", 17)
service.register_user("Пётр", 30)

print("Все пользователи:", service.get_all_users())
print("Совершеннолетние:", service.get_adults())
