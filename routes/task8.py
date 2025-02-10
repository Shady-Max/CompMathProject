from flask import Blueprint, render_template, request, session, jsonify
import solution.task8

task8_bp = Blueprint("task8", __name__)

@task8_bp.route("/", methods=["GET"])
def get():
    return render_template("task8.html", output=None, graph=None)

@task8_bp.route("/", methods=["POST"])
def post():
    return render_template("task8.html", output=None, graph=None)