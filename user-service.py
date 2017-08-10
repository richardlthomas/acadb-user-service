"""
AcaDB User Service

Author: Rick Thomas
Created on August 9, 2017
"""

import user_db_config
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

db_user = user_db_config.db_user
db_user_pass = user_db_config.db_user_password

app.config['MONGO_HOST'] = db_user+':'+db_user_pass+'@aea-userdb-shard-00-00-diqae.mongodb.net:27017,aea-userdb-' \
                                                    'shard-00-01-diqae.mongodb.net:27017,aea-userdb-shard-00-02-diqae' \
                                                    '.mongodb.net:27017/aea-userdb?ssl=true&replicaSet=aea-userdb-' \
                                                    'shard-0&authSource=admin'

def home():
    users = mongo.db.users.find()
    return render_template('index.html', users=users)

if __name__=='__main__':
   app.run(debug=True)
