from flask import *
from conn import *
app = Flask(__name__, static_folder="static")

@app.route('/',methods=['GET'])
def index():
    querySelect="SELECT * FROM eventosculturales"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(querySelect)
    eventos = cursor.fetchall()
    print(eventos)

    return render_template('index.html',eventos=eventos)

@app.route('/debug')
def debug_db():
    query = "SELECT id_evento, nombre_evento, latitud, longitud FROM eventosculturales"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    eventos = cursor.fetchall()
    
    return jsonify(eventos)  # Esto imprimirá la lista en formato JSON

if __name__ == "__main__":
    app.run(debug=True)