# Criando a aplicação admin do banco da aplicação

## 1. Instala as dependências
```bash
pip install sqlalchemy
pip install sqladmin
pip install sqladmin[full]
pip install Alembic
```
## 2. Cria o banco de dados de testes
- example_database.py

## 3. Cria o módulo de modelos (contendo user)
- models.py

## 4. Cria o main.py para subir a aplicação FastAPI
- main.py

## 5. Cria o admin.py para controla a autenticação na aplicação principal do FastAPI
- admin.py

## 6. Cria o diretório migrations
```bash
mkdir migrations
```

## 7. Inicializa o diretório via alembic
```bash
alembic init migration
```

## 8. Faz as correções no env.py gerado pelo alembic

Observação 1: 
- É preciso corrigir o link dos módulos no diretório de migrations do alembic

```python
import sys
sys.path = ['', '..'] + sys.path[1:]

#Para só então importar 
from example_database import Base
```

Observação 2: 
- Foi preciso comentar o arquivo de configuração de log, pois no script original dá erro, pois não existe configuração de log do alembic

## 9. Migrar os modelos para o database
```bash
alembic revision --autogenerate -m "Add table Users"
```

## 10. Aplica as modificações no database
```bash
alembic upgrade head
```

## 11. Executa a aplicação principal do FastAPI
```bash
uvicorn main:app --reload
```

## 12. Faz o login com o usuário (armando/armando) criado no banco de exemplo. 
- http://localhost:8000/admin

## Mais detalhes em SQLAdmin
- https://aminalaee.dev/sqladmin