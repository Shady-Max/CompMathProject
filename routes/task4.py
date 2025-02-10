from flask import Blueprint, render_template, request, session, jsonify
import solution.task4

task4_bp = Blueprint("task4", __name__)

@task4_bp.route("/", methods=["GET"])
def get():
    return render_template("task4.html", output=None, graph=None)

@task4_bp.route("/", methods=["POST"])
def post():
    return render_template("task4.html", output=None, graph=None)