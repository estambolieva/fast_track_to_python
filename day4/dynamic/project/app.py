from flask import Flask
from flask import render_template

from pymongo import MongoClient
import json
# tools for using json module for bson documents
from bson import json_util

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'donorschoose'
COLLECTION_NAME = 'projects'
FIELDS = {'school_state': True, 'resource_type': True, 'poverty_level': True, 'date_posted': True,
          'total_donations': True, '_id': False}

# index page of local server - displays Hello World
# shows results in localhost:5000/
@app.route("/")
def index():
    return render_template("index.html")

# query MongoDB to retrieve donorschoose records
# show results in localhost:5000/donorschoose/projects
@app.route("/donorschoose/projects")
def donorschoose_projects():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS)
    json_projects = []
    logger.info("projects are " + str(projects))
    for project in projects:
        json_projects.append(project)
    # if specified, default is a function that gets called on objects otherwise not serializable
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)