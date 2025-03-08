from flask import *
from conn import *
import re
from validaciones import *
app = Flask(__name__, static_folder="static")
app.secret_key = "supersecreto"

@app.route('/',methods=['GET'])
def index():
    eventos=show()
    return render_template('index.html',eventos=eventos)

@app.route('/sorted', methods=['GET','POST'])
def sorted_events():
    fecha_evento = request.form['fecha_evento']
    precio = int(request.form['precio'])
    tipo_evento = request.form['tipo_evento']
    error,eventos=validacion_precio_validacion_fecha(fecha_evento,precio,tipo_evento)
    if error:
        flash(error, "warning")
        return redirect(url_for("index"))
    return render_template('index.html', eventos=eventos)

if __name__ == "__main__":
    app.run(debug=True)