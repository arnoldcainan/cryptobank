import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

# Esta fixture cria um cliente HTTP assíncrono para testar a API
@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

@pytest.fixture(scope="module")
async def client():
    # ASGITransport conecta direto na aplicação FastAPI sem precisar subir servidor
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c