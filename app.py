from flask import Flask, request
from operations import add, sub, mult, div

# Put your app in here.

app = Flask(__name__)

@app.get('/add/')
def add_request():
    """return sum of a and b"""

    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)

    return f"a + b = {add(a,b)}"

@app.get('/sub/')
def sub_request():
    """return difference of a minus b"""

    a = request.args.get('a')
    b = request.args.get('b')
    return f"a - b = {sub(a,b)}"