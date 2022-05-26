import psycopg2
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer,String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_restful import Api
from sqlalchemy import func

engine = create_engine('postgresql://admin:1234@127.0.0.1:5432/flask_netology') #подключение к базе
Base = declarative_base()

class Advertisement(Base):
    __tablename__ = 'Advertisement'
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    description = Column(String(80))
    created_date = Column(DateTime, server_default=func.now())
    author = Column(String(80))

Base.metadata.create_all(engine)

app = Flask('app')


@app.route('/check/')
def check():
    response = jsonify({'status':'ok'})
    return response

@app.route("/login/", methods=["POST"])
def login():
    json_data = request.json
    return jsonify({
                    'json': json_data,
                    'header':dict(request.headers),
                    'qs':dict(request.args)
    })

app.run()
