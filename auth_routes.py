from fastapi import APIRouter, Depends, status, HTTPException
from dependencies import pegar_sessao
from models import Usuario
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["Autenticação"])

@auth_router.get('/')
async def home():
    ''' Rota padrão de autenticação. '''
    
    return {
        'mensagem': 'Você acessou a rota padrão de autenticação!', 
        'autenticado': False
    }
    

@auth_router.post('/criar_conta', status_code=status.HTTP_201_CREATED)
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)):
    # Filtrando todos os usuários com o email especificado.
    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()
    
    if usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Esse email já está sendo utilizado por outro usuário')
    
    # Cria um Hash a partir da senha do usuário
    senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
    
    # Criando o novo usuário
    novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
    
    # Adicionando o usuário na sessão
    session.add(novo_usuario)
    
    # Enviando as alterações para o banco de dados
    session.commit()
    
    return {
        'mensagem': f'Usuário cadastrado com sucesso {usuario_schema.email}!'}

# @auth_router.post('/login')
# async def login():