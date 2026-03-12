class Book:
    """Класс для представления информации о книге."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """Возвращает строку с описанием книги для печати."""
        return f"«{self.title}», автор: {self.author}"

    def to_format_string(self):
        """Подготавливает строку для сохранения в файл (например, через разделитель)."""
        return f"{self.title};{self.author}"

if __name__ == "__main__":
    book1 = Book("Преступление и наказание", "Ф. Достоевский")
    print(book1)
