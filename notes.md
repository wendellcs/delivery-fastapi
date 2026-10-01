# FastAPI

## 🐍 Conceitos Gerais

### def vs async def

***Como o FastAPI lida com uma rota declarada com a sintaxe def convencional 
(síncrona) versus uma rota declarada com async def?***

- Funções ***def*** normais são executadas em um threadpool externo, enquanto 
***async def*** rodam diretamente no event loop.

- O FastAPI gerencia rotas síncronas ( def ) enviando a execução para um pool
de threads para não bloquear o loop de eventos assíncrono principal.


### Depends

```python 
    async def criar_conta(nome: str, email: str, senha: str, session = Depends(pegar_sessao)):
```

- ***Depends***: Cria uma dependência que a rota precisa antes de executar sua lógica.


### Generators

- Um objeto que produz valores um por vez, conforme precisamos deles, em vez de criar tudo de uma vez na memória

#### Ex: Generator vs Lista

```python
    numeros = [1, 2, 3, 4, ..., 1000000]
    # Todos os valores são criados e ficam armazenados na memória.
```

```python
    def numeros():
        for i in range(1, 1000001):
            yield i

    # Os números são produzidos conforme são solicitados.
```

### Return vs Yield

- ***return*** entrega um valor e encerra a função. ***yield*** entrega um valor, mas permite que a função continue depois.

```python
    def get_db():
    db = SessionLocal()

    try:
        # O yield serve para pausar uma função temporariamente e entregar um valor.
        yield db
    finally:
        db.close()
```


## 🔐 Criptografia

### bcrypt

- O bcrypt é utilizado para proteger senhas através de hashing. A senha original não é armazenada no banco de dados.

#### Como funciona:

1. O usuário cria uma senha.
2. O bcrypt transforma a senha em um ***hash*** usando um ***salt*** aleatório.
3. O hash é armazenado no banco de dados, e não a senha original.
4. No login, a senha digitada é comparada com o hash armazenado.
5. Se corresponder, a senha está correta.

***Importante***: bcrypt não descriptografa a senha. Ele verifica se a senha informada corresponde ao hash armazenado.

#### O que é Hash?

- Um hash é o resultado de passar uma informação por uma função matemática que gera uma espécie de "impressão digital" daquela informação.

```
    Senha:
    "banana123"
            ↓
        HASH
            ↓
    "8f4a7c91..."
```

- É unidirecional, não desfazemos o hash.

#### O que é Salt?

- O salt é um valor aleatório adicionado à senha antes/durante o processo de hashing.

Imagine duas pessoas usando exatamente a mesma senha:

```
    João  → "123456"
    Maria → "123456"
```

Sem salt, um sistema de hash determinístico poderia produzir:
```
João  → 123456 → HASH → ABCDEF
Maria → 123456 → HASH → ABCDEF
```
Isso revela que os dois usuários possuem a mesma senha.

Com salt, temos algo como:

```
João:
"123456" + salt_A
        ↓
      HASH
        ↓
     ABCDEF

Maria:
"123456" + salt_B
        ↓
      HASH
        ↓
     XYZ123
```

Agora:
```
mesma senha
    +
salts diferentes
    ↓
hashes diferentes
```

O bcrypt combina essas ideias.

De forma simplificada:

```
Senha
  ↓
Salt aleatório
  ↓
bcrypt
  ↓
Hash
  ↓
Banco de dados
```

### Sobre o bcrypt

- Criando e configurando um objeto que será responsável por trabalhar com o bcrypt:

```python
    bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    # CryptContext -> Funciona como um gerenciador de algoritmos de hash de senha.

    # schemes -> Escolhe o algoritmo que vou trabalhar

    # deprecated='auto' -> permite que o Passlib gerencie automaticamente esquemas considerados   obsoletos.
```


## HTTP Response

- Resposta que a API envia de volta ao cliente.

### Status code

#### Raise

- Usamos sempre que houver algo errado.

```python 
    # Lançando uma exceção com raise
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Mensagem de erro')
```