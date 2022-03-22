from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import read_json, write_json 


app = Flask(__name__)
CORS(app)


@app.route("/leer", methods=["GET"])
def leer_usuarios():
    return jsonify(read_json())


@app.route("/crear", methods=["POST"])
def crear_usuario():
    alias = request.args["alias"]
    email = request.args["email"]
    name = request.args["name"]
    
    user = {
        "alias":alias,
        "email":email,
        "name":name
    }       

    data = read_json()
    data["users"].append(user)
    write_json(data)
    
    return jsonify(data)


@app.route("/buscar", methods=["GET"])
def buscar_usuario():
    if request.method == "GET":
       email = request.args["email"] 
       data = read_json()        

       for user in data["users"]:
            if user["email"] == email:
               return jsonify(user) 


@app.route("/borrar", methods=["DELETE"])
def borrar_usuario():
    if request.method == "DELETE":
       email = request.args["email"] 
       data = read_json()        
       
       for idx, user in enumerate(data["users"]):
            if user["email"] == email:
               data["users"].pop(idx) 
       
       write_json(data)        
        
       return jsonify("usuario eliminado...") 
        


app.run(host="127.0.0.1", debug=True)