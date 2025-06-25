from flask import Flask, request, jsonify

app= Flask(__name__)
dati=[{"id": "1235","timestamp": "12:21", "num": 30},
      {"id": "1235","timestamp": "12:21", "num": 30},
      {"id": "1235","timestamp": "12:21", "num": 30},
      {"id": "1235","timestamp": "12:21", "num": 30},
      {"id": "1235","timestamp": "12:21", "num": 30},
      {"id": "1235","timestamp": "12:21", "num": 30},
      {"id": "1235","timestamp": "12:21", "num": 30}]

@app.route('/restituisce', methods=['GET'])
def res():
   return jsonify(dati)

@app.route('/riceve', methods=['POST'])
def riceve():
    
    if request.is_json:
        data = request.get_json()
        dati.append(data)
        return jsonify(data), 201
    else:
         return jsonify({"error": "Il corpo della richiesta non è JSON"}), 400

if __name__ == '__main__':
   app.run( debug=True, host='0.0.0.0', port=5000)
    