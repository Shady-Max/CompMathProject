from flask import Blueprint, render_template, request, session, jsonify
import tasks.task1

task1_bp = Blueprint("task1", __name__)

@task1_bp.route("/", methods=["GET"])
def get():
    left_interval = session.get("task1:left_interval", 1)
    right_interval = session.get("task1:right_interval", 2)
    number_of_points = session.get("task1:points", 500)
    approx_root = session.get("task1:approx_root", 2)

    context = {
        "left_interval": left_interval,
        "right_interval": right_interval,
        "points": number_of_points,
        "approx_root": approx_root,
        "output": None,
        "graph": None
    }

    return render_template("task1.html", **context)

@task1_bp.route("/", methods=["POST"])
def post():
    left_interval = float(request.form.get("left_interval"))
    right_interval = float(request.form.get("right_interval"))
    number_of_points = int(request.form.get("points"))
    approx_root = session.get("task1:approx_root", 2)
    session["task1:left_interval"] = left_interval
    session["task1:right_interval"] = right_interval
    session["task1:points"] = number_of_points

    tasks.task1.a = left_interval
    tasks.task1.b = right_interval
    tasks.task1.points = number_of_points
    graph_json = tasks.task1.solution()
    context = {
        "left_interval": left_interval,
        "right_interval": right_interval,
        "points": number_of_points,
        "approx_root": approx_root,
        "output": [
            ("Absolute error", "need's to be calculated", "absolute_error")
        ],
        "graph": graph_json
    }
    return render_template("task1.html", **context)

@task1_bp.route('/error_calc', methods=["POST"])
def error_calculation():
    approx_root = float(request.form.get("approx_root"))
    session["task1:approx_root"] = approx_root
    absolute_error = tasks.task1.task1_calculate_error(approx_root)
    return jsonify({"Absolute error": (absolute_error, "absolute_error")})