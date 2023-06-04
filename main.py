from flask import Flask, render_template, send_file
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    # читаем таблицу Excel
    df = pd.read_excel("students.xlsx")
    # передаем DataFrame в шаблон и возвращаем HTML-страницу
    return render_template("table.html", table=df.to_html())

@app.route("/download")
def download():
    # отправляем файл Excel
    return send_file("students.xlsx", as_attachment=True)

if __name__ == "__main__":
    app.run()