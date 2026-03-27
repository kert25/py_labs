import sqlite3

conn = sqlite3.connect("lab7.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS staff (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        dept_id INTEGER,
        FOREIGN KEY (dept_id) REFERENCES departments(id)
    )
""")

cur.execute("INSERT INTO departments (name) VALUES (?)", ("IT",))
cur.execute("INSERT INTO departments (name) VALUES (?)", ("HR",))
cur.execute("INSERT INTO staff (name, dept_id) VALUES (?, ?)", ("Иванов", 1))
cur.execute("INSERT INTO staff (name, dept_id) VALUES (?, ?)", ("Петрова", 2))
cur.execute("INSERT INTO staff (name, dept_id) VALUES (?, ?)", ("Сидоров", 1))
conn.commit()

cur.execute("""
    SELECT staff.name, departments.name
    FROM staff
    JOIN departments ON staff.dept_id = departments.id
""")

print("Сотрудник | Отдел")
for row in cur.fetchall():
    print(f"{row[0]} | {row[1]}")

conn.close()
