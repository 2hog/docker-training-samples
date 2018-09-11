import redis
import sec
from flask import Flask


app = Flask(__name__)
redis_client = redis.StrictRedis.from_url(sec.load("REDIS_URL"))

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/count")
def count():
    result = redis_client.incr("counter")
    return f"Hello World! You're number {result}"
