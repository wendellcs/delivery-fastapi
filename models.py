from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# Criando a conexão com o banco de dados
db = create_engine('sqlite:///./database/banco.db')

# Criando a base de dados
Base = declarative_base()

# Cria as classes/tabelas do banco

class Usuario(Base):
    # Definindo o nome da tabela
    __tablename__ = 'usuarios'
    
    # primary_key -> Define a coluna como chave primária.
    # autoincrement -> O banco de dados vai gerar um id único para cada usuário.
    # nullable -> Não permite que o campo seja nulo. 
    # default -> Define um valor padrão para o campo.
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)
    email = Column('email', String, nullable=False )
    senha = Column('senha', String)
    ativo = Column('ativo', Boolean)
    admin = Column('admin', Boolean, default=False)
    
    def __init__(self, nome, email, senha, ativo = True, admin = False):
        self.nome = nome 
        self.email = email 
        self.senha = senha 
        self.ativo = ativo
        self.admin = admin
        

class Pedido(Base):
    __tablename__ = 'pedidos'
    
    # STATUS_PEDIDOS = (
    #     ('PENDENTE', 'PENDENTE'),
    #     ('CANCELADO', 'CANCELADO'),
    #     ('FINALIZADO', 'FINALIZADO')
    # )
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    status = Column('status', String ) # Pendente, cancelado, finalizado
    usuario = Column('usuario', ForeignKey('usuarios.id'))
    preco = Column('preco', Float)
    # itens = 
    
    def __init__(self, usuario, status = 'PENDENTE', preco = 0):
        self.usuario = usuario
        self.status = status
        self.preco = preco
    
    
class ItemPedido(Base):
    __tablename__ = 'itens_pedido'
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    quantidade = Column('quantidade', Integer)
    sabor = Column('sabor', String)
    tamanho = Column('tamanho', String)
    preco_unitario = Column('preco_unitario', Float)
    pedido = Column('pedido', ForeignKey('pedidos.id'))
    
    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido


# Executa a criação dos metadados do seu banco ( cria o banco de dados e as tabelas ).

