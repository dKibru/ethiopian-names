from peewee import *
from pprint import pprint
import json

db = SqliteDatabase('../database/names.db')
class BaseModel(Model):
    class Meta:
        database = db
class Ethiopian(BaseModel):
    name = CharField(unique=True)
    sex = CharField()

db.connect()


# CREATE DATABASE
# db.create_tables([Ethiopian])


# CHANGE TO LOWERCASE
# for person in Ethiopian.select():
# 	name = person.name[0]+person.name.lower()[1:len(person.name)]
# 	if person.name != name:
# 		print(name)
# 		person.name = name
# 		person.save()


# WRITE TO JSON FILE
# file = open("../data/data1.json", "w")
# i = 1
# for person in Ethiopian.select():
# 	file.write('{"name":"'+person.name+'","sex":"'+person.sex+'"},')


# READ FROM JSON AND POPULATE THE DB
# file = open("../data/data.json", "r")
# loaded_json = json.loads(file.read())
# for x in loaded_json:
# 	g = loaded_json[x].get('gender')
# 	if g == 'MALE':
# 		Ethiopian.create(name=x,sex='M')
# 	if g == 'FEMALE':
# 		Ethiopian.create(name=x,sex='F')









db.close
