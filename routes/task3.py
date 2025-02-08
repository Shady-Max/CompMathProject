from flask import Blueprint, render_template, request, session, jsonify
import tasks.task3

task3_bp = Blueprint("task3", __name__)

@task3_bp.route("/", methods=["GET"])
def get():
    return render_template("task3.html", output=None, graph=None)

@task3_bp.route("/", methods=["POST"])
def post():
    return render_template("task3.html", output=None, graph=None)