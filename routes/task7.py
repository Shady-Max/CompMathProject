from flask import Blueprint, render_template, request, session, jsonify
import solution.task7

task7_bp = Blueprint("task7", __name__)

@task7_bp.route("/", methods=["GET"])
def get():
    return render_template("task7.html", output=None, graph=None)

@task7_bp.route("/", methods=["POST"])
def post():
    return render_template("task7.html", output=None, graph=None)