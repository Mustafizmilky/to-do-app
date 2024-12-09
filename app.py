from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
TASK_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return f.read().splitlines()

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        f.write("\n".join(tasks))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks")
def tasks():
    return jsonify(load_tasks())

@app.route("/add", methods=["POST"])
def add_task():
    task = request.json.get("task")
    if task:
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)
    return "", 200

@app.route("/delete/<int:index>", methods=["POST"])
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return "", 200

if __name__ == "__main__":
    app.run(debug=True)