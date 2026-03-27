from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Купить молоко", "done": False},
    {"id": 2, "title": "Выучить Python", "done": False},
]

HTML = """
<!DOCTYPE html>
<html>
<head><title>Список задач</title></head>
<body>
    <h1>Список задач</h1>
    <form method="post" action="/add">
        <input type="text" name="title" placeholder="Новая задача" required>
        <button type="submit">Добавить</button>
    </form>
    <ul>
        {% for task in tasks %}
            <li>
                {{ task.title }}
                <a href="/delete/{{ task.id }}">[удалить]</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML, tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    if title:
        tasks.append({
            "id": len(tasks) + 1,
            "title": title,
            "done": False
        })
    return redirect("/")


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect("/")


app.run(debug=True)
