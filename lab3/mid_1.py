import os


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write_file(self, content):
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Записано в {self.filename}")

    def read_file(self):
        if not os.path.exists(self.filename):
            return "Файл не найден"
        with open(self.filename, "r", encoding="utf-8") as f:
            return f.read()

    def append_to_file(self, content):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(content + "\n")
        print(f"Добавлено в {self.filename}")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"Книга: {self.title}, Автор: {self.author}"


file = FileManager("books.txt")
book1 = Book("Мастер и Маргарита", "Михаил Булгаков")
book2 = Book("Герой нашего времени", "Михаил Лермонтов")

file.append_to_file(book1.get_info())
file.append_to_file(book2.get_info())

print("\nСодержимое файла:")
print(file.read_file())
