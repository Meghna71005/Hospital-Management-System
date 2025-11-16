from flask import Flask,  render_template

app= Flask(__name__)

# defining routes

@app.route("/")
def home():
     return render_template("index.html", active="home")
 
@app.route("/login")
def login():
    return render_template("login.html", active="login")

@app.route("/register")
def register():
    return render_template("register.html", active="register")

@app.route("/admin")
def admin():
    return render_template("admin_dashboard.html")

@app.route("/patient")
def patient():
     return render_template("patient_dashboard.html")

@app.route("/doctor")
def doctor():
     return render_template("doctor_dashboard.html")
    
if __name__ == "__main__":
    app.run(debug=True)