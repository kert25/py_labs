import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    number = request.query_params.get("number")
    if number:
        result = int(number) ** 2
        return f"""
        <html>
        <body>
            <h1>Введите число</h1>
            <form method="get" action="/">
                <input type="number" name="number" placeholder="Число">
                <button type="submit">Посчитать квадрат</button>
            </form>
            <p>Квадрат {number} = {result}</p>
        </body>
        </html>
        """
    return """
    <html>
    <body>
        <h1>Введите число</h1>
        <form method="get" action="/">
            <input type="number" name="number" placeholder="Число">
            <button type="submit">Посчитать квадрат</button>
        </form>
    </body>
    </html>
    """


uvicorn.run(app, host="127.0.0.1", port=8000)
