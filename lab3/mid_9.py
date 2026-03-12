import os


class FileManager:
    """Класс для базовых операций с текстовыми файлами."""

    def __init__(self, filename):
        self.filename = filename

    def write_file(self, content):
        """Создает файл и записывает в него текст (перезаписывая существующий)."""
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Файл '{self.filename}' успешно записан.")
        except Exception as e:
            print(f"Ошибка при записи: {e}")

    def read_file(self):
        """Читает содержимое файла и возвращает его."""
        if not os.path.exists(self.filename):
            return f"Ошибка: Файл '{self.filename}' не найден."

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"Ошибка при чтении: {e}"

    def append_to_file(self, content):
        """Добавляет текст в конец существующего файла."""
        try:
            with open(self.filename, "a", encoding="utf-8") as f:
                f.write("\n" + content)
            print(f"Данные добавлены в '{self.filename}'.")
        except Exception as e:
            print(f"Ошибка при добавлении: {e}")


if __name__ == "__main__":
    my_file = FileManager("lab_work.txt")

    my_file.write_file("Первая строка лабораторной работы.")

    my_file.append_to_file("Вторая строка добавлена методом append.")

    print("\nСодержимое файла:")
    print(my_file.read_file())
