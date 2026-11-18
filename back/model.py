from datetime import datetime 
from flask_sqlalchemy import SQLALchemy 

db = SQLALchemy()


class Produto(db.Model): 
    __tablename__ = "Produtos"
    id = db.column(db.Integer, primary_key=True)
    nome = db.column(db.String(120), nullaable=False)
    descricao = db.column(db.texte)
    categoria = db.column(db.String(80))
    preco = db.column(db.Float, nullable=False)
    estoque = db.column(db.Integer, defalt=0)
    imagem = db.column(db.String(255))