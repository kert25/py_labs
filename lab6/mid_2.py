from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><title>Приветствие</title></head>
<body>
    <form method="post">
        <input type="text" name="username" placeholder="Введите имя">
        <button type="submit">Отправить</button>
    </form>
    {% if name %}
        <h1>Привет, {{ name }}!</h1>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def greet():
    name = None
    if request.method == "POST":
        name = request.form.get("username")
    return render_template_string(HTML, name=name)


app.run(debug=True)
