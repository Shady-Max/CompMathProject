from flask import Blueprint, render_template, request, session, jsonify
import tasks.task2

task2_bp = Blueprint("task2", __name__)

@task2_bp.route("/", methods=["GET"])
def get():
    return render_template("task2.html", output=None, graph=None)

@task2_bp.route("/", methods=["POST"])
def post():
    return render_template("task2.html", output=None, graph=None)