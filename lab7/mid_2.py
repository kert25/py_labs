import sqlite3

conn = sqlite3.connect("lab7.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        salary INTEGER
    )
""")

cur.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)",
            ("Иванов Иван", "Программист", 80000))
cur.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)",
            ("Петрова Мария", "Дизайнер", 70000))
conn.commit()

cur.execute("SELECT * FROM employees")
for row in cur.fetchall():
    print(f"ID: {row[0]}, Имя: {row[1]}, "
          f"Должность: {row[2]}, Зарплата: {row[3]}")

conn.close()
