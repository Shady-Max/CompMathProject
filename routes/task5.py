from flask import Blueprint, render_template, request, session, jsonify
import solution.task5

task5_bp = Blueprint("task5", __name__)

@task5_bp.route("/", methods=["GET"])
def get():
    x = [0,1,2,3,4]
    y = [0,1,4,9,16]
    points = session.get("task5:points", 5)
    x = session.get("task5:x", x)
    y = session.get("task5:y", y)
    context= {
        "points": points,
        "x": x,
        "y": y
    }
    return render_template("task5.html", **context)

@task5_bp.route("/points", methods=["POST"])
def points_post():
    x = [0,1,2,3,4]
    y = [0,1,4,9,16]
    points = int(request.form["points"])
    session["task5:points"] = points
    x = session.get("task5:x", x)
    y = session.get("task5:y", y)
    context = {
        "points": points,
        "x": x,
        "y": y
    }
    return render_template("task5.html", **context)

@task5_bp.route("/", methods=["POST"])
def post():
    size = session.get("task5:points", 5)
    x = [float(request.form[f'x_{i}']) for i in range(size)]
    y = [float(request.form[f'y_{i}']) for i in range(size)]
    session["task5:x"] = x
    session["task5:y"] = y
    graph = solution.task5.polynomial_curve_fitting(x,y)
    context = {
        "points": size,
        "x": x,
        "y": y,
        "graph": graph
    }
    return render_template("task5.html", **context)