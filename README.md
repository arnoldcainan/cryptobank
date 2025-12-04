# 🏦 Cryptobank API

API de alta performance para gestão de portfólio de criptoativos, desenvolvida com **FastAPI** e **Arquitetura Assíncrona**.

O sistema permite gestão de usuários, criação de carteiras de investimento e consulta de saldo com conversão em tempo real para Bitcoin (BTC), consumindo dados de mercado ao vivo.

## 🚀 Tech Stack

- **Linguagem:** Python 3.11
- **Framework Web:** FastAPI (Async)
- **Banco de Dados:** PostgreSQL
- **ORM:** SQLAlchemy 2.0 (Async)
- **Migrações:** Alembic
- **Validação:** Pydantic V2
- **Containerização:** Docker & Docker Compose
- **Http Client:** Httpx (Chamadas assíncronas externas)

## 🏗️ Arquitetura

O projeto segue os princípios da **Clean Architecture** simplificada, focando em desacoplamento e escalabilidade:

- **API/**: Controladores e rotas.
- **Core/**: Configurações e segurança.
- **Crud/**: Regras de acesso ao banco.
- **Services/**: Integrações externas (CoinGecko API).
- **Schemas/**: Contratos de dados (DTOs) com Pydantic.

## ⚡ Como Rodar

### Pré-requisitos
- Docker e Docker Compose instalados.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/cryptobank.git](https://github.com/SEU_USUARIO/cryptobank.git)
   cd cryptobank