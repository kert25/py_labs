from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, item_id):
        pass

    @abstractmethod
    def delete(self, item_id):
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        self.items = []
        self.next_id = 1

    def add(self, item):
        item["id"] = self.next_id
        self.next_id += 1
        self.items.append(item)
        return item

    def get_all(self):
        return self.items

    def get_by_id(self, item_id):
        for item in self.items:
            if item["id"] == item_id:
                return item
        return None

    def delete(self, item_id):
        self.items = [i for i in self.items if i["id"] != item_id]


repo = InMemoryRepository()

repo.add({"name": "Python"})
repo.add({"name": "JavaScript"})
repo.add({"name": "Go"})

print("Все языки:", repo.get_all())
print("Язык с ID 2:", repo.get_by_id(2))

repo.delete(1)
print("После удаления:", repo.get_all())
