from flask import Flask, render_template
from logic import get_category, categories

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('./index.html', category=get_category(), categories=categories)

@app.route("/<category>")
def detail(category):
    if category not in categories:
        return "Abeg Gettat"
    return render_template('./index.html', category=get_category(category), categories=categories)