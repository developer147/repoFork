from flask import Flask
from markupsafe import escape
from github import Github

app = Flask(__name__)

g = Github("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")

g = Github(base_url="https://localhost:5001/api/v3", login_or_token="access_token")

@app.route("/pyGithub")
def py_github():
    for repo in g.get_user().get_repos():
        print(repo.name)
        repo.edit(has_wiki=False)
        # to see all the available attributes and methods
        print(dir(repo))

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/projects")
def projects():
    return 'The project page'

@app.route("/about")
def about():
    return 'The about page'

