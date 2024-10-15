from flask import Flask, redirect, render_template, flash, request
import hashlib


local_username = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
local_password = "96cae35ce8a9b0244178bf28e4966c2ce1b8385723a96a6b838858cdd6ca0a1e"
autorization = False

def hashing(text):
  return hashlib.sha256(text.encode('utf-8')).hexdigest()

app = Flask(__name__)
app.secret_key = "9875321046"

@app.route('/')
def hello():
  return render_template('main.html')

@app.route("/admin_panel")
def admin_panel():
  if not autorization:
    return redirect("/")
   
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
  global autorization
  
  if request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    print(hashing(username))
    
    if (hashing(username) == local_username) and (hashing(password) == local_password): 
      autorization = True
      return redirect("/admin_panel")
    else:
      flash("Логин или пароль неверен", 'success')
  return render_template("admin.html")

app.run(debug=True)