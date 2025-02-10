from flask import Blueprint, render_template, request, session, jsonify
import solution.task6

task6_bp = Blueprint("task6", __name__)

@task6_bp.route("/", methods=["GET"])
def get():
    x = [5,6,7,8]
    y = [25,36,49,64]
    x = session.get("task6:x", x)
    y = session.get("task6:y", y)
    points = session.get("task6:points", 4)
    x_target = session.get("task6:x_target", 5.5)
    context = {
        "points": points,
        "x": x,
        "y": y,
        "x_target": x_target
    }
    return render_template("task6.html", **context)

@task6_bp.route("/points", methods=["POST"])
def points_post():
    x = [5,6,7,8]
    y = [25,36,49,64]
    points = int(request.form["points"])
    session["task6:points"] = points
    x = session.get("task6:x", x)
    y = session.get("task6:y", y)
    x_target = session.get("task6:x_target", 5.5)
    context = {
        "points": points,
        "x": x,
        "y": y,
        "x_target": x_target
    }
    return render_template("task6.html", **context)

@task6_bp.route("/", methods=["POST"])
def post():
    points = session.get("task6:points", 4)
    x = [float(request.form[f'x_{i}']) for i in range(points)]
    y = [float(request.form[f'y_{i}']) for i in range(points)]
    x_target = float(request.form["x_target"])
    session["task6:x"] = x
    session["task6:y"] = y
    session["task6:x_target"] = x_target
    output, graph = solution.task6.solution(x, y, x_target)
    context = {
        "points": points,
        "x": x,
        "y": y,
        "x_target": x_target,
        "output": output,
        "graph": graph
    }
    return render_template("task6.html", **context)