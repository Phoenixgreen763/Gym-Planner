import os
from flask import (
    Flask, flash, render_template,
    redirect, jsonify, request, session, url_for)
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
        username = session.get("user")
        return render_template("home.html", username=username)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("home"))  # Redirect to 'home' after successful login
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("home"))  # Redirect to 'home'

    return render_template("register.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile", methods=["GET", "POST"])
def profile():
    username = session.get("user")

    return render_template("profile.html", username=username)


@app.route("/planner", methods=["GET", "POST"])
def planner():
    if "user" in session:
        username = session["user"]
        exercises = list(mongo.db.exercises.find({"created_by": username}))
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("planner.html", username=username, exercises=exercises, days=days, categories=categories)
    else:
        return redirect(url_for("login"))


@app.route("/")
@app.route("/get_exercises")
def get_exercises():
    if "user" in session:
        exercises = list(mongo.db.tasks.find({"created_by": session["user"]}))
        return render_template("planner.html", exercises=exercises)


@app.route("/add_exercise", methods=["GET", "POST"])
def add_exercise():
    if request.method == "POST":
        exercise = {
            "day_name": request.form.get("day_name"),
            "category_name": request.form.get("category_name"),
            "exercise_name": request.form.get("exercise_name"),
            "exercise_description": request.form.get("exercise_description"),
            "created_by": session["user"]
        }
        mongo.db.exercises.insert_one(exercise)
        flash("Exercise Successfully Added")
        return redirect(url_for("planner"))

    days = mongo.db.days.find().sort("day_name", 1)
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_exercise.html", categories=categories, days=days)


@app.route("/edit_exercise/<exercise_id>", methods=["GET", "POST"])
def edit_exercise(exercise_id):
    if request.method == "POST":
        submit = {
            "day_name": request.form.get("day_name"),
            "category_name": request.form.get("category_name"),
            "exercise_name": request.form.get("exercise_name"),
            "exercise_description": request.form.get("exercise_description"),
            "created_by": session["user"]
        }
        mongo.db.exercise.update_one(
            {"_id": ObjectId(exercise_id)},
            {"$set": submit}
        )
        flash("Exercise Updated")
        return redirect(url_for("planner"))


@app.route("/delete_exercise/<exercise_id>")
def delete_exercise(exercise_id):
    mongo.db.exercises.delete_one({"_id": ObjectId(exercise_id)})
    flash("Exercise Deleted")
    return redirect(url_for("planner"))


@app.route("/calendar")
def calendar():

    return render_template("calendar.html")


@app.route('/events', methods=["GET"])
def get_events():
    events = list(mongo.db.events.find())
    for event in events:
        event["_id"] = str(event["_id"])  # Convert ObjectId to string for JSON serialization
    return jsonify(events)


@app.route("/events", methods=["POST"])
def add_event():
    if request.method == "POST":
        event_name = request.form.get("event_name")
        event_start_date = request.form.get("event_start_date")
        if not event_name or not event_start_date:
            return jsonify({'status': False, 'msg': 'Please enter all required details.'})
        
        event = {
            'event_name': event_name,
            'event_start_date': event_start_date
        }
        
        mongo.db.events.insert_one(event)
        return jsonify({'status': True, 'msg': 'Event added successfully!'})


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)