from flask import Flask
from flask import request
import requests
from flask import jsonify

app = Flask(__name__)

DEBUG = True
app.debug = DEBUG
app.use_debugger = DEBUG

TOKEN = '064968cdbc6a496571d814dd2769aa1d2ae137d2'

REPO_OWNER = 'dotgc'
REPO_NAME = 'git-email'

@app.route("/email_hook", methods=['GET', 'POST'])
def email_hook():
    req_data = request.get_json()
    try:
        head_commit = req_data['head_commit']
    except Exception as e:
        head_commit = {}
    head_commit_id = head_commit['id']
    commit_url = 'https://api.github.com/repos/%s/%s/git/commits/%s'
    diff_url = commit_url % (REPO_OWNER, REPO_NAME, head_commit_id)
    return jsonify({'diff': diff_url, 'token': TOKEN})

def fetch_url(url):
    resp = requests.get(url)

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
