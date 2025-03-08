import pymysql
def get_db_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="eventos",
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None
    