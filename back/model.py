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


    def to_dect(self): 
        return{
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "categoria": self.categoria,
            "preco": self.categoria,
            "estoque": self.estoque,
            "imagem": self.imagem
        }
    

class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.column(db.Integer, primary_key=True)
    nome = db.column(db.String(120), nullable=False)
    email = db.column(db.String(120), unique=True)
    telefone = db.column(db.String(20))
    endereco = db.column(db.String(255))

    pedidos = db.relationship(
        "Pedido", 
        back_populates="cliente",
        lazy=True
    )

    def to_dect(self):
        return{
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "endereco": self.endereco

        }
    

class Pedido(db.Model):
    __tablename__ = "pedidos"

    id = db.column(db.Integer, primary_key=True)
    data = db.column(db.DateTime, defalt=datetime.now)
    status = db.column(db.String(50), defalt="Pendente")
    total = db.column(db.Float, defalt=0.0)

    cliente_id = db.column(
        db.Integer,
        db.ForeignKey("clientes.id"),
        nullable=True 
    )

    Cliente = db.relationship(
        "Cliente",
        back_populates="Pedido"
    )

    itens = db.relationship(
        "ItemPedido",
        back_populates = "Pedido",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return{
            "id": self.id,
            "data": self.data.strftime("%d/%m/%y %H:%M"),
            "status": self.status,
            "total": self.total,
            "cliente_id": self.cliente_id,
            "cliente": self.cliente.nome if self.cliente else None,
            "itens": [item.to_dict() for item in self.itens]
    }  




