from flask import Blueprint, render_template, request, session, jsonify
import solution.task4
import numpy as np

task4_bp = Blueprint("task4", __name__)

@task4_bp.route("/", methods=["GET"])
def get():
    A = [[3.0, -2.0, 5.0],
         [-4.0, 6.0, 7.0],
         [-5.0, 8.0, 9.0]]
    A = session.get("task4:A", A)
    context = {
        "A": A
    }
    return render_template("task4.html", **context)

@task4_bp.route("/", methods=["POST"])
def post():
    size = 3
    A = [[float(request.form[f'matrix_{i}_{j}']) for j in range(size)] for i in range(size)]
    session["task4:A"]=A
    L,U = solution.task4.lu_factorization(np.array(A, dtype=float))
    context = {
        "A": A,
        "L": np.round(L, 4),
        "U": np.round(U, 4)
    }
    return render_template("task4.html", **context)