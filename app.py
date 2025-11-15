from flask import Flask

app= Flask(__name__)

# defining routes

@app.route("/")
def index:
    print("Home page")