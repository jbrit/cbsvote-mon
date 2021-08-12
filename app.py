from flask import Flask, render_template
# from tochukwu's script import fetch_category_details, and vote for category with post & env key


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('./index.html')