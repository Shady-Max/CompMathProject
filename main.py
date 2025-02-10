from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import routes

app = Flask(__name__)
app.config.from_object("config")

app.register_blueprint(routes.task1_bp, url_prefix="/task/1")
app.register_blueprint(routes.task2_bp, url_prefix="/task/2")
app.register_blueprint(routes.task3_bp, url_prefix="/task/3")
app.register_blueprint(routes.task4_bp, url_prefix="/task/4")
app.register_blueprint(routes.task5_bp, url_prefix="/task/5")
app.register_blueprint(routes.task6_bp, url_prefix="/task/6")
app.register_blueprint(routes.task7_bp, url_prefix="/task/7")
app.register_blueprint(routes.task8_bp, url_prefix="/task/8")

@app.route("/")
@app.route("/home")
def index():
    return redirect("/task/1")

if __name__ == "__main__":
    app.run()