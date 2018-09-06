import os
from flask import Flask

app = Flask(__name__)
if os.path.exists('/config/greet-who'):
    with open('/config/greet-who', 'r') as fin:
        greet_who = fin.read().strip()
else:
    greet_who = os.getenv('GREET_WHO', 'World')

@app.route('/')
def hello_world():
    return f'Hello, {greet_who}!'
