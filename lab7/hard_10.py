import unittest
import sqlite3


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            )
        """)
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_insert(self):
        self.cur.execute("INSERT INTO users (name, age) VALUES (?, ?)",
                         ("Иван", 25))
        self.conn.commit()
        self.cur.execute("SELECT * FROM users WHERE name = 'Иван'")
        result = self.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], "Иван")
        self.assertEqual(result[2], 25)

    def test_select_all(self):
        self.cur.execute("INSERT INTO users (name, age) VALUES (?, ?)",
                         ("Мария", 30))
        self.cur.execute("INSERT INTO users (name, age) VALUES (?, ?)",
                         ("Пётр", 22))
        self.conn.commit()
        self.cur.execute("SELECT * FROM users")
        results = self.cur.fetchall()
        self.assertEqual(len(results), 2)

    def test_delete(self):
        self.cur.execute("INSERT INTO users (name, age) VALUES (?, ?)",
                         ("Анна", 28))
        self.conn.commit()
        self.cur.execute("DELETE FROM users WHERE name = 'Анна'")
        self.conn.commit()
        self.cur.execute("SELECT * FROM users WHERE name = 'Анна'")
        result = self.cur.fetchone()
        self.assertIsNone(result)


unittest.main()
