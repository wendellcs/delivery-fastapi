from pydantic import BaseModel
from typing import Optional

# Schemas -> classes usadas para forçar a tipagem dos dados.
# Objetivo de usar schemas: velocidade e integridade do sistema.

# Classe que vai definir quais informações um usuário tem que ter.
class UsuarioSchema(BaseModel):
    nome: str 
    email: str 
    senha: str 
    
    # Cria um valor opcional do tipo booleano
    ativo: Optional[bool]
    admin: Optional[bool]
    
    # Permite que o Pydantic leia os dados diretamente dos atributos de um objeto, como um objeto 
    # criado pelo SQLAlchemy, e transforme esse objeto em uma Schema.
    class Config:
        from_attributes = True
        # Permite transformar um objeto do banco em uma resposta baseada nessa Schema.
        
class PedidoSchema(BaseModel):
    id_usuario: int
    
    class Config:
        from_attributes = True