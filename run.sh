#!/bin/sh

# Para a execução se algum comando falhar
set -e

# Roda as migrações
echo "Aplicando migrações no banco de dados..."
alembic upgrade head

# Inicia o servidor usando a porta do Railway ($PORT)
echo "Iniciando servidor Uvicorn na porta $PORT..."
uvicorn app.main:app --host 0.0.0.0 --port $PORT