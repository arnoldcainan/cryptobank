# .PHONY garante que o make não confunda o comando com um arquivo de mesmo nome
.PHONY: up down logs test migrate shell db-reset help

# --- Comandos Básicos ---
up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

# --- Desenvolvimento ---
test:
	docker compose exec -T app pytest -v

# Uso: make migrate msg="nome_da_migracao"
migrate:
	docker compose exec app alembic revision --autogenerate -m "$(msg)"
	docker compose exec app alembic upgrade head

# Entra no terminal do container (útil para debug)
shell:
	docker compose exec app /bin/bash

# --- Perigo (Reseta tudo) ---
db-reset:
	docker compose down -v
	docker compose up -d --build
	@echo "Aguardando banco reiniciar..."
	@sleep 5
	docker compose exec app alembic upgrade head

help:
	@echo "Comandos disponiveis:"
	@echo "  make up        - Sobe os containers"
	@echo "  make down      - Derruba os containers"
	@echo "  make logs      - Ve os logs em tempo real"
	@echo "  make test      - Roda os testes automatizados"
	@echo "  make migrate msg=\"texto\" - Cria e aplica nova migracao"
	@echo "  make shell     - Entra no terminal do container"
	@echo "  make db-reset  - APAGA O BANCO e recria do zero"