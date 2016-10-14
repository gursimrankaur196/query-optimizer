from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/ONE'
db = SQLAlchemy(app)

class def_repository(db.Model):
	__tablename__ = 'def_repository'
	id = db.Column('id' , db.Integer,primary_key=True)
	name = db.Column('name' , db.String)
	description = db.Column('description', db.String)
	keyword = db.Column('keyword',db.String)

	def __init__(self,id,name,description,keyword):
		self.id=id
		self.name=name
		self.description=description
		self.keyword=keyword
		