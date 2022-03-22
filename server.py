from flask import Flask, request, jsonify
import json


app = Flask(__name__)

json_path = "mock.json"


@app.route("/users")
def get_users():
    with open(json_path, "r") as rfile:
        try:
            json_data = json.load(rfile)
        except:
            return jsonify("error read json")  
        finally:
            rfile.close()   
            
    return jsonify(json_data)


@app.route("/add", methods=["POST"])
def add_user():
    alias = request.args["alias"]
    email = request.args["email"]
    name = request.args["name"]

    user = {
        "alias": alias,
        "email": email,
        "name": name
    }
    
    with open(json_path, "r") as rfile:
        json_data = json.load(rfile)
    
    json_data["users"].append(user)  
       
    json_users = json.dumps(json_data)  
        
    with open(json_path, "w") as wfile:
        wfile.write(json_users)        

    return jsonify(json_users)


@app.route("/del", methods=["DELETE"])
def del_user():
    if request.method == "DELETE":
    
     alias = request.args["alias"]  
                 
     with open(json_path,"r") as rfile:
        json_data = json.load(rfile)
         
    for idx, user in enumerate(json_data["users"]):
        if user["alias"] == alias:
           json_data["users"].pop(idx)             
        
    with open(json_path, "w") as wfile:
        wfile.write(json.dumps(json_data)) 
        
    return jsonify(json_data)       
     

@app.route("/up", methods=["PUT"])
def put_user():
    if request.method == "PUT":
       alias = request.args["alias"]  
       email = request.args["email"]  
       name = request.args["name"]  
       
    with open(json_path, "r") as rfile:
        try: 
            json_data = json.load(rfile) 

            for _, user in enumerate(json_data["users"]):
                 if user["alias"] == alias:
                    user["email"] = email 
                    user["name"] = name        
        except:
             return jsonify("error read json")
        
    with open(json_path, "w") as wfile:
        try:
            wfile.write(json.dumps(json_data))       
        except:
            return jsonify("error write json")
        finally:
            wfile.close()
        
    return jsonify(json_data)         


@app.route("/user", methods=["GET"])
def get_user():
    
    alias = request.args["alias"]
    
    try:
        with open(json_path, "r") as rfile:
           json_data = json.load(rfile)
    except:
        return jsonify("error read file")       
    finally:
        rfile.close()    
    
    for idx, user in enumerate(json_data["users"]):
        if user["alias"] == alias:
           return jsonify(json_data["users"][idx])     
            
app.run(host="127.0.0.1", debug=True)
