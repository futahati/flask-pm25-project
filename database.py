import pandas as pd
import requests, io
import pymysql
from datetime import datetime
import urllib3
import os
from dotenv import load_dotenv

load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_latest_data():
    conn, cursor = open_db()

    result = {"success": True, "message": None, "columns": None, "rows": None}

    if not conn:
        result["success"] = False
        result["message"] = "資料庫開啟失敗！"
        return result

    # sql = "SELECT * FROM data LIMIT 500;"
    sql = """
    SELECT * FROM data where datacreationdate=
    (SELECT max(datacreationdate) FROM data);
    """

    # 取得資料庫裡最新的日期
    # sql = "SELECT max(datacreationdate) FROM data;"
    try:
        cursor.execute(sql)

        # 取得資料欄位名稱
        # print(cursor.description)
        columns = [col[0] for col in cursor.description]

        rows = cursor.fetchall()
        result["success"] = True
        result["columns"] = columns
        result["rows"] = rows

        return result

    except Exception as e:
        result["success"] = False
        result["message"] = f"資料庫查詢失敗，原因：{e}"

        return result
    finally:
        conn.close()


# 建立雲端連線
# 使用 MySQL(PyMySQL) 語法
def open_db():
    # host=os.getenv("HOST") ← os.getenv()本地端dotenv使用
    try:
        conn = pymysql.connect(
            host=os.environ.get("HOST"),
            port=int(os.environ.get("PORT")),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            database=os.environ.get("NAME"),
            ssl={"ca": None},
        )

        cursor = conn.cursor()

        return conn, cursor

    except Exception as e:
        print(e)

    return None, None


print(get_latest_data())

if __name__ == "__main__":
    pass
