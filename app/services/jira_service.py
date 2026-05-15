import httpx

from app.core.config import settings


async def get_issue(issue_key):

    url = f"{settings.JIRA_BASE_URL}/rest/api/3/issue/{issue_key}"

    async with httpx.AsyncClient() as client:

        response = await client.get(
            url,
            auth=(settings.JIRA_EMAIL, settings.JIRA_TOKEN)
        )

    return response.json()