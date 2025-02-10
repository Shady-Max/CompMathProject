from flask import Blueprint, render_template, request, session, jsonify
import solution.task7

task7_bp = Blueprint("task7", __name__)

@task7_bp.route("/", methods=["GET"])
def get():
    x = [5,6,7,8]
    y = [25,36,49,64]
    x = session.get("task6:x", x)
    y = session.get("task6:y", y)
    points = session.get("task6:points", 4)
    context = {
        "points": points,
        "x": x,
        "y": y,
    }
    return render_template("task7.html", **context)

@task7_bp.route("/", methods=["POST"])
def post():
    points = session.get("task7:points", 4)
    x = [float(request.form[f'x_{i}']) for i in range(points)]
    y = [float(request.form[f'y_{i}']) for i in range(points)]
    session["task7:x"] = x
    session["task7:y"] = y
    output = solution.task7.solution(x,y)
    context = {
        "points": points,
        "x": x,
        "y": y,
        "output": output,
    }
    return render_template("task7.html", **context)

@task7_bp.route("/points", methods=["POST"])
def points_post():
    x = [5,6,7,8]
    y = [25,36,49,64]
    points = int(request.form["points"])
    session["task7:points"] = points
    x = session.get("task7:x", x)
    y = session.get("task7:y", y)
    context = {
        "points": points,
        "x": x,
        "y": y,
    }
    return render_template("task7.html", **context)