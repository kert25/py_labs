import os


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write_file(self, content):
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Файл {self.filename} перезаписан.")

    def read_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                return f.read()
        return "Файл не найден."

    def append_to_file(self, content):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(content + "\n")
        print(f"Данные добавлены в {self.filename}.")


file = FileManager("test.txt")
file.write_file("Первая строка.")
file.append_to_file("Вторая строка.")

print("\nСодержимое файла:")
print(file.read_file())
