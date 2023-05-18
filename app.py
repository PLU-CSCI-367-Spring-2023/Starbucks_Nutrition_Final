import psycopg2
from flask import Flask, request, render_template
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
    nutr_id = request.args.get("id", "")
    item = request.args.get("item", "")
    calories = request.args.get("calories", "")
    fat = request.args.get("fat", "")
    carb = request.args.get("carbs", "")
    fiber = request.args.get("fiber", "")
    protein = request.args.get("protein", "")
    nutr_type = request.args.get("type", "")

    from_where_clause = """
    select nutr_id, item, calories, fat, carb, fiber, protein, nutr_type
    from nutrition 
    """

    params = {
        "nutr_id": f"%{nutr_id}%",
        "item": f"%{item}%",
        "calories": f"%{calories}%",
        "fat": f"%{fat}%",
        "car": f"%{carb}%",
        "fiber": f"%{fiber}%",
        "protein": f"%{protein}%",
        "nutr_type": f"%{nutr_type}"

    }

    with conn.cursor() as cur:
        cur.execute(f"select n.nutr_id as id, n.item as item {from_where_clause} limit 10",
                    params)
        results = list(cur.fetchall())

        cur.execute(f"select count(*) as count {from_where_clause}",
                    params)
        count = cur.fetchone()["count"]

        return render_template("nutrition.html",
                               params=request.args,
                               result_count=count,
                               nutrition=results)
