from flask import Flask, request, jsonify
import mysql.connector
import json
app= Flask(__name__)
data= mysql.connector.connect(
     host="localhost",
  user="root",
  password="Giaco",
  database="stage"
)

@app.route('/restituisce', methods=['GET'])
def res():
    cursor = data.cursor()
    cursor.execute("SELECT * FROM specifiche")
    results = cursor.fetchall()

    return json.dumps(results)
  

@app.route('/riceve', methods=['POST'])
def riceve():
    
    if request.is_json:
        ric= request.get_json()
        
        val1=ric["ID"]
        val2=ric["Tempo"]
        val3=ric["Inquinanti"]
        cursor = data.cursor()
        query = "INSERT INTO specifiche (ID, Tempo, Inquinanti) VALUES (%s, %s, %s)"
        cursor.execute(query, (val1, val2, val3))
        data.commit()
        return jsonify({"message": "Dati inseriti con successo"}), 201
        
    else:
        return jsonify({"error": "Il corpo della richiesta non è JSON"}), 400
    


@app.route('/taglia', methods=['DELETE'])  
def taglia():
    ric= request.get_json()
    cursor = data.cursor()
    
    cursor.exceute ("SELECT * FROM specifiche WHERE ID = %s", (ric["ID"]))
    result = cursor.fetchone()
    if result is None:
        return jsonify({"error": "ID non trovato"}), 404
    else:
        cursor.execute("DELETE FROM specifiche WHERE ID = %s", (ric["ID"],))
        data.commit()
        return jsonify({"message": "Dati eliminati con successo"}), 200
    

@app.route('/modifica', methods=['PUT'])
def modifica():
    ric = request.get_json()
    cursor = data.cursor()
    
    cursor.execute("SELECT * FROM specifiche WHERE ID = %s", (ric["ID"],))
    result = cursor.fetchone()
    
    if result is None:
        return jsonify({"error": "ID non trovato"}), 404
    else:
        query = "UPDATE specifiche SET Tempo = %s, Inquinanti = %s WHERE ID = %s"
        cursor.execute(query, (ric["Tempo"], ric["Inquinanti"], ric["ID"]))
        data.commit()
        return jsonify({"message": "Dati aggiornati con successo"}), 200



if __name__ == '__main__':
   app.run( debug=True, host='0.0.0.0', port=5000)
    
