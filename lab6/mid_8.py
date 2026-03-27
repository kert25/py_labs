import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

HTML = """
<!DOCTYPE html>
<html>
<head><title>FastAPI</title></head>
<body>
    <h1>Введите число</h1>
    <form method="get" action="/square">
        <input type="number" name="number" placeholder="Число">
        <button type="submit">Посчитать квадрат</button>
    </form>
    {% if number is not none %}
        <p>Квадрат {{ number }} = {{ result }}</p>
    {% endif %}
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    number = request.query_params.get("number")
    result = int(number) ** 2 if number else None
    content = HTML.replace("{% if number is not none %}", "")
    content = content.replace("{% endif %}", "")
    content = content.replace("{{ number }}", str(number or ""))
    content = content.replace("{{ result }}", str(result or ""))
    return content


uvicorn.run(app, host="127.0.0.1", port=8000)
