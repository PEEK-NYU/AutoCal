import sys
import json
import pymongo as pm
import bson.json_util as bsutil

#from pymongo.server_api import ServerAPi

# import mongo_conect as mc

client = pm.MongoClient()
print(client)

db = client = ["CalendarDB"]
print(db)

#db = client ["ChatDB"]
#print(db)
#
#collect_nm = sys.argv[2]
#print(f"colect_nm=}")
#collection = db[collect_nm]

# Prof Cal: "You won't need this for the project, but to run it locally on computer to see what it does"
