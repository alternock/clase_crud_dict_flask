from flask import jsonify
import json

connect_db = "database.json"


def read_json():
    try:
       with open(connect_db, "r") as rdb:
           data = json.load(rdb)            
           return data
    except:
        return None
    finally:    
        rdb.close()


def write_json(data):
    with open(connect_db, "w") as wdb:
        try:
            wdb.write(json.dumps(data))
        except:
            return jsonify("write read file")    
        finally:
            wdb.close()        
