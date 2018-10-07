from flask import Flask,jsonify
import os
import csv

app = Flask(__name__)


@app.route("/")
@app.route("/datos/centros-teleton")
def datosCentrosTeleton():
    with open('BDHack.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        return jsonify(getJSONfromDataCRITS(reader))
    return "Hola"

# Obtains data from the table read from csv and parse to JSON
def getJSONfromDataCRITS(reader):
    json  = {}
    contador = 0
    for row in reader:
        json[contador] = {
                "Descripcion": row["Descripcion"],
                "Datos":{
                    "Recursos_necesarios": row["Recursos necesarios 2018"],
                    "Ingresos_comprometidos": row["Ingresos comprometidos"],
                    "Porcentaje_esperado_de_cumplimiento": row ["porcentaje esperado de cumplimiento"],
                    "Ingresos_esperados": row["Ingresos esperados"],
                    "Recursos_a_recaudar": row["Recursos necesarios a recaudar en Evento Teleton"],
                    "Capacidad_de_ninos": row["Capacidad ninos"],
                    "Costo_anual_promedio_por_paciente": row["Costo anual promedio por paciente"],
                    "Num_de_Ninos_por_cubrir_con_donativo": row["# de Ninos por cubrir con donativo"]      
                    }
            }
        contador += 1
    return json


@app.route("/datos/banamex")
def datosBanamex():
    path = 'Datos/2016/Banamex'
    nomArchivo = obtenerUltimoArchivo(path ,'.teleton.')
    with open(path + '/' + nomArchivo) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
    return "Hola"

#obtiene el ultimo archivo mandado por la institucion
def obtenerUltimoArchivo(institucion,referencia):
    f = []
    ultimo = ""
    mayor = 0
    for (dirpath, dirnames, filenames) in os.walk(institucion):
        f.extend(filenames)
        break
    for file in f:
        #buscamos teleton para conocer la version del archivo
        ind = file.find(referencia)
        #si es el mayor, es el ultimo
        if( file[ind + len(referencia) : ind + len(referencia) + 4] > mayor):
            mayor = file[ind + 9 : ind + 13]
            ultimo = file
    return ultimo


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
