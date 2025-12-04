import pytest
from unittest.mock import patch, AsyncMock, MagicMock
from app.services.market_data import get_crypto_price


# --- TESTE UNITÁRIO (MOCK) ---
# Aqui testamos a função de cotação SEM ir na internet de verdade.
# Usamos 'patch' para fingir que a CoinGecko respondeu.
@pytest.mark.asyncio
async def test_unit_get_crypto_price_success():
    mock_data = {"bitcoin": {"usd": 100000}}

    # 1. Criamos o Mock da RESPOSTA (o objeto que o .get retorna)
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_data

    # 2. Fazemos o Patch usando AsyncMock no método .get
    # Isso é essencial porque 'client.get' é uma função async
    with patch("app.services.market_data.httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_response

        price = await get_crypto_price("bitcoin", "usd")

        assert price == 100000
        assert mock_get.called


# --- TESTE DE INTEGRAÇÃO (ROTA REAL) ---
# Aqui testamos se a API cria o usuário e salva no banco de verdade.
@pytest.mark.asyncio
async def test_integration_create_user(client):
    user_data = {
        "email": "tester@cryptobank.com",
        "password": "senha_de_teste",
        "full_name": "QA Engineer"
    }

    response = await client.post("/api/v1/users/", json=user_data)

    # Esperamos 201 (Criado) ou 400 (se já rodou o teste antes e o email existe)
    assert response.status_code in [201, 400]

    if response.status_code == 201:
        data = response.json()
        assert data["email"] == user_data["email"]
        assert "id" in data
        assert "password" not in data  # Segurança: senha não pode voltar!