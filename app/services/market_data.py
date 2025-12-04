import httpx


async def get_crypto_price(coin_id: str = "bitcoin", currency: str = "usd") -> float:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10.0)
            response.raise_for_status()
            data = response.json()
            return data.get(coin_id, {}).get(currency, 0.0)
        except Exception as e:
            print(f"Erro ao buscar preço: {e}")
            return 0.0