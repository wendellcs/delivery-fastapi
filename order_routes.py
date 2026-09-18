from fastapi import APIRouter

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