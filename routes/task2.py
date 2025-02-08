from flask import Blueprint, render_template, request, session, jsonify
import tasks.task2

task2_bp = Blueprint("task2", __name__)

@task2_bp.route("/", methods=["GET"])
def get():
    left_interval = session.get("task2:left_interval", 1)
    right_interval = session.get("task2:right_interval", 2)
    tol = session.get("task2:tol", 1e-6)
    context = {
        "left_interval": left_interval,
        "right_interval": right_interval,
        "tol": tol
    }
    return render_template("task2.html", **context)

@task2_bp.route("/", methods=["POST"])
def post():
    left_interval = float(request.form.get("left_interval"))
    right_interval = float(request.form.get("right_interval"))
    tol = float(request.form.get("tol"))
    session["left_interval"] = left_interval
    session["right_interval"] = right_interval
    session["tol"] = tol
    tasks.task2.init(left_interval, right_interval, tol)
    result = tasks.task2.solution()
    context = {
        "left_interval": left_interval,
        "right_interval": right_interval,
        "tol": tol,
        **result
    }
    return render_template("task2.html", **context)