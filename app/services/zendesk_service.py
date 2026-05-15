import httpx

from app.core.config import settings


async def create_ticket(data):

    url = f"{settings.ZENDESK_BASE_URL}/api/v2/tickets.json"

    async with httpx.AsyncClient() as client:

        response = await client.post(
            url,
            json=data,
            auth=(
                f"{settings.ZENDESK_EMAIL}/token",
                settings.ZENDESK_TOKEN
            )
        )

    return response.json()