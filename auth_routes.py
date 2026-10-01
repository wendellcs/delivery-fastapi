from fastapi import APIRouter, Depends
from dependencies import pegar_sessao
from models import Usuario


auth_router = APIRouter(prefix="/auth", tags=["Autenticação"])

@auth_router.get('/')
async def home():
    ''' Rota padrão de autenticação. '''
    
    return {
        'mensagem': 'Você acessou a rota padrão de autenticação!', 
        'autenticado': False
    }
    

@auth_router.post('/criar_conta', status_code=201)
async def criar_conta(nome: str, email: str, senha: str, session = Depends(pegar_sessao)):
    # Filtrando todos os usuários com o email especificado.
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    
    if usuario:
        return {
            'mensagem': 'Esse email já está sendo utilizado por outro usuário'}
    
    # Criando o novo usuário
    novo_usuario = Usuario(nome, email, senha)
    # Adicionando o usuário na sessão
    session.add(novo_usuario)
    # Enviando as alterações para o banco de dados
    session.commit()
    
    return {
        'mensagem': 'Usuário cadastrado com sucesso!'}
