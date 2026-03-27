class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append({"title": title, "done": False})

    def get_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True


class TaskView:
    def show_tasks(self, tasks):
        print("Список задач:")
        for i, task in enumerate(tasks):
            status = "[x]" if task["done"] else "[ ]"
            print(f"  {i}. {status} {task['title']}")

    def show_message(self, message):
        print(message)


class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, title):
        self.model.add_task(title)
        self.view.show_message(f"Задача '{title}' добавлена")

    def show_tasks(self):
        tasks = self.model.get_tasks()
        self.view.show_tasks(tasks)

    def complete_task(self, index):
        self.model.complete_task(index)
        self.view.show_message(f"Задача {index} выполнена")


model = TaskModel()
view = TaskView()
controller = TaskController(model, view)

controller.add_task("Выучить MVC")
controller.add_task("Сделать лабу")
controller.complete_task(0)
controller.show_tasks()
