from flask import Blueprint, render_template, request, session, jsonify
import solution.task3
import numpy as np

task3_bp = Blueprint("task3", __name__)

@task3_bp.route("/", methods=["GET"])
def get():
    size = 3
    A = [[1, 1, 1], 
        [1, 0, 1], 
        [0, 1, 1]]
    b = [9, 3, 7]
    A = session.get("task3:A", A)
    b = session.get("task3:b", b)
    iter = session.get("task3:iter", 500)
    tol = session.get("task3:tol", 1e-6)
    contex = {
        "A": A,
        "b": b,
        "iter": iter,
        "tol": tol
    }
    return render_template("task3.html", **contex)

@task3_bp.route("/", methods=["POST"])
def post():
    size = 3
    A = [[float(request.form[f'matrix_{i}_{j}']) for j in range(size)] for i in range(size)]
    b = [float(request.form[f'vector_{i}']) for i in range(size)]
    iter = int(request.form["iter"])
    tol = float(request.form["tol"])
    session["task3:A"] = A
    session["task3:b"] = b
    session["task3:iter"] = iter
    session["task3:tol"] = tol
    output = solution.task3.solution(np.array(A, dtype=float), np.array(b, dtype=float), iter, tol)
    print(output)
    contex = {
        "A": A,
        "b": b,
        "iter": iter,
        "tol": tol,
        "output": output
        }
    
    return render_template("task3.html", **contex)