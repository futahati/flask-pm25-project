from flask import Flask, render_template, jsonify
import database

# 取得本地端的伺服器__name__
app = Flask(__name__)


@app.route("/api/data/<county>")
def api_data_by_county(county):
    rows = database.get_data_by_county(county)["rows"]

    return jsonify(rows)


@app.route("/api/counties")
def api_counties():
    counties = database.get_counties()["rows"]

    counties = [c[0] for c in counties]

    # jsonify：解析json格式
    return jsonify(counties)


@app.route("/")
def index():

    result = database.get_latest_data()

    counties = database.get_counties()["rows"]
    counties = [c[0] for c in counties]

    return render_template("index.html", result=result, counties=counties)


if __name__ == "__main__":
    # pass
    # 最後一行，要執行
    app.run(debug=True)
