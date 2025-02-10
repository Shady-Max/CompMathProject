from flask import Blueprint, render_template, request, session, jsonify
import solution.task8

task8_bp = Blueprint("task8", __name__)

@task8_bp.route("/", methods=["GET"])
def get():
    a = session.get("task8:a", 0)
    b = session.get("task8:b", 3.14)
    n = session.get("task8:n", 6)
    context = {
        "a": a,
        "b": b,
        "n": n
    }
    return render_template("task8.html", **context)

@task8_bp.route("/", methods=["POST"])
def post():
    a = float(request.form["a"])
    b = float(request.form["b"])
    n = int(request.form["n"])
    session["task8:a"] = a
    session["task8:b"] = b
    session["task8:n"] = n
    output = solution.task8.simpsons_rule(solution.task8.f, a, b, n)
    context = {
        "a": a,
        "b": b,
        "n": n,
        "output": output
    }
    return render_template("task8.html", **context)