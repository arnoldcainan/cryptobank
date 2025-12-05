# 🏦 Cryptobank API

API profissional de alta performance para gestão de portfólio de criptoativos, desenvolvida com foco em **Clean Architecture**, **Segurança** e **Escalabilidade**.

O sistema implementa um fluxo completo de **Autenticação JWT (OAuth2)**, permitindo que usuários gerenciem carteiras e consultem saldos convertidos em Bitcoin em tempo real (via integração assíncrona com CoinGecko).

![CI Status](https://github.com/arnoldcainan/cryptobank/actions/workflows/ci.yml/badge.svg)

## 🚀 Destaques Técnicos

- **Core:** Python 3.11, FastAPI (Async), Pydantic V2.
- **Banco de Dados:** PostgreSQL + AsyncPG + SQLAlchemy 2.0.
- **Segurança:** Autenticação JWT (OAuth2 Password Flow), Hash de senhas com Bcrypt.
- **Integração:** Consumo de APIs externas com Httpx (Non-blocking I/O).
- **Qualidade:** Testes automatizados (Pytest) rodando em Pipeline de CI (GitHub Actions).
- **Infra:** Docker & Docker Compose.

## 🏗️ Arquitetura

O projeto segue uma arquitetura modular inspirada em Clean Architecture:

```text
📂 app
├── 📂 api          # Endpoints e Injeção de Dependência
├── 📂 core         # Configurações, Segurança (JWT) e Env Vars
├── 📂 crud         # Camada de Acesso a Dados
├── 📂 models       # Modelos do ORM (SQLAlchemy)
├── 📂 schemas      # Contratos de Dados (Pydantic)
└── 📂 services     # Regras de Negócio e Integrações Externas
📂 tests            # Testes Unitários e de Integração
📂 .github          # Pipelines de CI/CD
