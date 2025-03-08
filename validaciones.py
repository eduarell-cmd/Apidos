import re
from flask import *
from conn import *
from datetime import datetime
app.secret_key = "supersecreto"

def show():
    querySelect="SELECT * FROM eventosculturales"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(querySelect)
    eventos = cursor.fetchall()
    return eventos

def validacion_precio_validacion_fecha(fecha_evento,precio,tipo_evento):
    patron = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(patron, fecha_evento):
        return "Favor de ingresar la fecha en formato aaaa-mm-dd", None
    try:
        # Convertir la cadena a un objeto datetime para verificar si la fecha es válida
        datetime.strptime(fecha_evento, '%Y-%m-%d')
    except ValueError:
        return "La fecha ingresada no es válida", None
    if precio<0:
        return "Favor de no ingresar valores negativos", None
    conn = get_db_connection()
    cursor = conn.cursor()
    querySort="""SELECT * FROM eventosculturales WHERE fecha_evento = %s AND precio = %s AND tipo_evento = %s"""
    cursor.execute(querySort, (fecha_evento, precio, tipo_evento))
    eventos=cursor.fetchall()
    conn.close()
    print(f"Fecha Evento: {fecha_evento}, Precio: {precio}, Tipo Evento: {tipo_evento}")
    return None,eventos