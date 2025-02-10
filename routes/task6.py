from flask import Blueprint, render_template, request, session, jsonify
import solution.task6

task6_bp = Blueprint("task6", __name__)

@task6_bp.route("/", methods=["GET"])
def get():
    return render_template("task6.html", output=None, graph=None)

@task6_bp.route("/", methods=["POST"])
def post():
    return render_template("task6.html", output=None, graph=None)