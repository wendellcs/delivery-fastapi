from fastapi import APIRouter, Depends
from dependencies import pegar_sessao
from sqlalchemy.orm import Session
from schemas import PedidoSchema
from models import Pedido

order_router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

# No fastAPI, toda comunicação deve ser feita via JSON. Portanto, o retorno de uma função deve ser um dicionário.
# A função deve ser async.

@order_router.get('/')
async def pedidos():
    # Doc string, usado para explicar o que a função faz. 
    # No fastAPI, a doc string é usada para gerar a documentação da API.
    '''
        Rota padrão de pedidos.
        Todas as rotas dos pedidos precisam de autenticação.
    '''
    
    return {"mensagem": "Lista de pedidos"}

@order_router.post('/pedido')
async def criar_pedido(pedido_schema: PedidoSchema, session: Session =  Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario = pedido_schema.id_usuario)
    
    session.add(novo_pedido)
    session.commit()
    
    return {'mensagem': f'Pedido criando com sucesso. ID do pedido: {novo_pedido.id}'}