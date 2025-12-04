# 🏦 Cryptobank API

API profissional de alta performance para gestão de portfólio de criptoativos, com foco em segurança e escalabilidade.

O sistema implementa um fluxo completo de **Autenticação JWT (OAuth2)**, permitindo que usuários gerenciem carteiras e consultem saldos convertidos em Bitcoin em tempo real (via integração com CoinGecko).

![CI Status](https://github.com/SEU_USUARIO/cryptobank/actions/workflows/ci.yml/badge.svg)

## 🚀 Destaques Técnicos

- **Core:** Python 3.11, FastAPI (Async), Pydantic V2.
- **Banco de Dados:** PostgreSQL + AsyncPG + SQLAlchemy 2.0.
- **Segurança:** Autenticação JWT, Hash de senhas com Bcrypt.
- **Qualidade:** Testes automatizados (Pytest) rodando em Pipeline de CI (GitHub Actions).
- **Infra:** Docker & Docker Compose.

## ⚡ Guia Rápido (Makefile)

Para facilitar a produtividade, o projeto conta com comandos rápidos:

```bash
make up      # Sobe o ambiente (App + Banco)
make test    # Roda a suíte de testes (Unitários e Integração)
make logs    # Visualiza logs em tempo real
make down    # Encerra a aplicação