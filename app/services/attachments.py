import httpx

from app.core.config import settings


async def transfer_attachment(
    jira_attachment_url,
    filename
):

    upload_url = (
        f"{settings.ZENDESK_BASE_URL}"
        f"/api/v2/uploads.json?filename={filename}"
    )

    async with httpx.AsyncClient(timeout=60.0) as client:

        async with client.stream(
            "GET",
            jira_attachment_url,
            auth=(
                settings.JIRA_EMAIL,
                settings.JIRA_TOKEN
            )
        ) as jira_stream:

            response = await client.post(
                upload_url,
                content=jira_stream.aiter_bytes(),
                headers={
                    "Content-Type": "application/binary"
                },
                auth=(
                    f"{settings.ZENDESK_EMAIL}/token",
                    settings.ZENDESK_TOKEN
                )
            )

    return response.json()