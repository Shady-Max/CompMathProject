from flask import Blueprint, render_template, request, session, jsonify
import solution.task5

task5_bp = Blueprint("task5", __name__)

@task5_bp.route("/", methods=["GET"])
def get():
    return render_template("task5.html", output=None, graph=None)

@task5_bp.route("/", methods=["POST"])
def post():
    return render_template("task5.html", output=None, graph=None)