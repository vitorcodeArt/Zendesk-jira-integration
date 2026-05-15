from fastapi import APIRouter

from app.services.jira_service import get_issue

router = APIRouter(prefix="/webhooks/jira")


@router.post("/update")
async def jira_update(payload: dict):

    issue_key = payload["issue_key"]

    issue = await get_issue(issue_key)

    return {
        "message": "jira update recebido",
        "issue": issue
    }