import pymysql as PYM


# 資料庫參數設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "chadigo",
    "password": "Asd279604823",
    "db": "test",
    "charset": "utf8"
}

try:
    # 建立Connection物件
    conn = PYM.connect(**db_settings)

    # 建立Cursor物件
    with conn.cursor() as cursor:
        command = "SELECT * FROM `list`"
        cursor.execute(command)
        result = cursor.fetchall()
        print(result)
except Exception as ex:
     print(ex)