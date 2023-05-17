import psycopg2
from flask import Flask, request
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    "host=db dbname=postgres user=postgres password=postgres",
    cursor_factory=RealDictCursor)
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/nutrition')
def render_nutrition():
    id = request.args.get("id", "")
    item = request.args.get("item", "")
    calories = request.args.get("calories", "")
    fat = request.args.get("fat", "")
    carb = request.args.get("carbs", "")
    fiber = request.args.get("fiber", "")
    protein = request.args.get("protein", "")
    type = request.args.get("type", "")
