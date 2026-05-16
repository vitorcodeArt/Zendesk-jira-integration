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

def extract_description_text(description):

    if not description:
        return "Sem descrição"

    try:

        texts = []

        for block in description.get("content", []):

            for item in block.get("content", []):

                if item.get("type") == "text":

                    texts.append(
                        item.get("text", "")
                    )

        return "\n".join(texts)

    except Exception:

        return "Erro ao converter descrição"