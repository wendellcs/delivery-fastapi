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

